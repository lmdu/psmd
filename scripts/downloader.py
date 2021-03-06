import os
import sys
import csv
import json
import shutil
import requests

from ..config import Config

RPC_URL = 'http://localhost:6800/jsonrpc'
FASTA_DIR = os.path.join(Config.ROOT_DIR, 'fastas')
GFF_DIR = os.path.join(Config.ROOT_DIR, 'gffs')
INFO_DIR = os.path.join(Config.ROOT_DIR, 'info')
ASSEMBLY_REPORT_DIR = os.path.join(Config.ROOT_DIR, 'assemblyreports')

def get_dir(parent, subdir):
	folder = os.path.join(parent, subdir)
	if not os.path.exists(folder):
		os.makedirs(folder)
	return folder

def add_url_to_aria2(url, folder, name):
	json_request = json.dumps({
		'id': '',
		'jsonrpc': '2.0',
		'method': 'aria2.addUri',
		'params': [[url], {'dir': folder, 'out': name}]
	})

	response = requests.post(url=RPC_URL, data=json_request)

#infile, input best representive genomes
infile = sys.argv[1]

with open(os.path.join(INFO_DIR, infile), 'rt') as fh:
	reader = csv.reader(fh, delimiter='\t')
	for row in reader:
		acc = row[15]
		fas_url = row[16]
		gff_url = row[17]
		asr_url = fas_url.replace('genomic.fna.gz', 'assembly_report.txt')

		if ',' in row[4]:
			row[4] = row[4].split(',')[0]

		sub_dir = os.path.join(*row[3:6]).replace(' ', '_')
		fas_dir = get_dir(FASTA_DIR, sub_dir)
		gff_dir = get_dir(GFF_DIR, sub_dir)
		asr_dir = get_dir(ASSEMBLY_REPORT_DIR, sub_dir)

		#old_path = os.path.join(WORK_DIR, 'genomes', sub_dir, '{}.fna.gz'.format(acc))
		new_path = os.path.join(FASTA_DIR, sub_dir, '{}.fna.gz'.format(acc))
		if os.path.exists(new_path):
			continue
		
		#if os.path.exists(old_path):
		#	shutil.move(old_path, fas_dir)
		#else:
		add_url_to_aria2(fas_url, fas_dir, '{}.fna.gz'.format(acc))
		add_url_to_aria2(asr_url, asr_dir, '{}.assembly_report.txt'.format(acc))
		if gff_url:
			add_url_to_aria2(gff_url, gff_dir, '{}.gff.gz'.format(acc))

		print(acc)
		
