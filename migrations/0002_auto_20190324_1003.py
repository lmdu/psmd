# Generated by Django 2.0 on 2019-03-24 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psmd', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='issr',
            name='deletion',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='issr',
            name='insertion',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='issr',
            name='match',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='issr',
            name='substitution',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]