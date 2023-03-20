#!/usr/bin/env python3

import os
import time
import argparse
from rich import print

# Accept an argument before execution
parser = argparse.ArgumentParser(description='Sort files based on their file size.')
parser.add_argument('path', metavar='path', type=str, help='the path to the directory')
args = parser.parse_args()

#Get list of all files and directories from the argument
files = os.listdir(args.path)
files.sort(key=lambda x: os.path.getsize(os.path.join(args.path, x)))

index = 0;
for file in files:
	cTime = time.strftime('%I:%M:%S %p, %d/%m/%Y',time.localtime(os.path.getctime(os.path.join(args.path, file))))
	size = os.path.getsize(os.path.join(args.path, file))
	size_gb = size / (1024 * 1024 * 1024)
	index += 1
	if size < 1024 * 1024: #If size < 1MB
		size_kb = size / 1024
		print(f'[{index}] "{file}" - {cTime} | {size_kb:.2f} KB')
	elif size < 1024 * 1024 * 1024:
		size_mb = size /  (1024 * 1024)
		print(f'[{index}] "{file}" - {cTime} | {size_mb:.2f} MB')
	else:
		print(f'[{index}] "{file}" - {cTime} | {size_gb:.2f} GB')
