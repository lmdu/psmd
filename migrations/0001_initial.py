# Generated by Django 2.1.3 on 2019-03-01 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('level', models.SmallIntegerField(choices=[(1, 'Kingdom'), (2, 'Group'), (3, 'Subgroup')])),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PanMicrosatDB.Category')),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='CSSR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.IntegerField()),
                ('end', models.IntegerField()),
                ('complexity', models.IntegerField()),
                ('length', models.IntegerField()),
                ('structure', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'cssr',
            },
        ),
        migrations.CreateModel(
            name='Gene',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.IntegerField()),
                ('end', models.IntegerField()),
                ('gid', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('biotype', models.CharField(max_length=20)),
                ('dbxref', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'gene',
            },
        ),
        migrations.CreateModel(
            name='Genome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taxonomy', models.CharField(max_length=20)),
                ('species_name', models.CharField(max_length=255)),
                ('common_name', models.CharField(max_length=255)),
                ('biosample', models.CharField(max_length=15)),
                ('bioproject', models.CharField(max_length=15)),
                ('assembly_level', models.CharField(max_length=15)),
                ('assembly_accession', models.CharField(help_text='assembly accession in genbank', max_length=20)),
                ('download_accession', models.CharField(help_text='accession of used sequence file', max_length=20)),
                ('gene_count', models.IntegerField()),
                ('size', models.BigIntegerField()),
                ('gc_content', models.FloatField()),
                ('ssr_count', models.IntegerField()),
                ('ssr_frequency', models.FloatField()),
                ('ssr_density', models.FloatField()),
                ('cover', models.FloatField()),
                ('cm_count', models.IntegerField()),
                ('cm_frequency', models.FloatField()),
                ('cm_density', models.FloatField()),
                ('cssr_percent', models.FloatField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PanMicrosatDB.Category')),
            ],
            options={
                'db_table': 'genome',
            },
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('rowid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('accession', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'search',
            },
        ),
        migrations.CreateModel(
            name='Sequence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('accession', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'sequence',
            },
        ),
        migrations.CreateModel(
            name='SSR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.IntegerField()),
                ('end', models.IntegerField()),
                ('motif', models.CharField(max_length=6)),
                ('standard_motif', models.CharField(max_length=6)),
                ('ssr_type', models.SmallIntegerField(choices=[(1, 'Mono'), (2, 'Di'), (3, 'Tri'), (4, 'Tetra'), (5, 'Penta'), (6, 'Hexa')])),
                ('repeats', models.IntegerField()),
                ('length', models.IntegerField()),
            ],
            options={
                'db_table': 'ssr',
            },
        ),
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=30)),
                ('content', models.FloatField()),
            ],
            options={
                'db_table': 'summary',
            },
        ),
        migrations.CreateModel(
            name='CSSRAnnot',
            fields=[
                ('cssr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='PanMicrosatDB.CSSR')),
                ('location', models.SmallIntegerField(choices=[(1, 'CDS'), (2, 'exon'), (3, '3UTR'), (4, 'intron'), (5, '5UTR')])),
            ],
            options={
                'db_table': 'cssrannot',
            },
        ),
        migrations.CreateModel(
            name='CSSRMeta',
            fields=[
                ('cssr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='PanMicrosatDB.CSSR')),
                ('left_flank', models.CharField(max_length=100)),
                ('right_flank', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'cssrmeta',
            },
        ),
        migrations.CreateModel(
            name='SSRAnnot',
            fields=[
                ('ssr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='PanMicrosatDB.SSR')),
                ('location', models.SmallIntegerField(choices=[(1, 'CDS'), (2, 'exon'), (3, '3UTR'), (4, 'intron'), (5, '5UTR')])),
            ],
            options={
                'db_table': 'ssrannot',
            },
        ),
        migrations.CreateModel(
            name='SSRMeta',
            fields=[
                ('ssr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='PanMicrosatDB.SSR')),
                ('left_flank', models.CharField(max_length=100)),
                ('right_flank', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'ssrmeta',
            },
        ),
        migrations.AddField(
            model_name='ssr',
            name='sequence',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PanMicrosatDB.Sequence'),
        ),
        migrations.AddField(
            model_name='gene',
            name='sequence',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PanMicrosatDB.Sequence'),
        ),
        migrations.AddField(
            model_name='cssr',
            name='sequence',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PanMicrosatDB.Sequence'),
        ),
        migrations.AddField(
            model_name='ssrannot',
            name='gene',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PanMicrosatDB.Gene'),
        ),
        migrations.AddField(
            model_name='cssrannot',
            name='gene_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PanMicrosatDB.Gene'),
        ),
    ]
