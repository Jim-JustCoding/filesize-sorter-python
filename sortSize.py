#!/usr/bin/env python3

import os
import time
import argparse
from rich import print
from rich.style import Style
from console import console

# Accept an argument before execution
parser = argparse.ArgumentParser(prog='File Sorter', description='Sort files based on their file size.')
parser.add_argument('path', metavar='path', type=str, help='the path to the directory')
parser.add_argument('-e', '--extension', metavar='extension', type=str, help='the file extension to sort only', default=None)
args = parser.parse_args()

#Get list of all files and directories from the argument
files = os.listdir(args.path)
files.sort(key=lambda x: os.path.getsize(os.path.join(args.path, x)))

def file_to_array():
	with open("filename_extensions.txt", 'r') as f:
		lines = f.read().splitlines()
		for l in lines:
			if l == args.extension:
				print('Found extension')
				break
			else:
				continue

def extFileSorter():
	index = 1;
	console.print('[green]Extension to filter:', args.extension)
	time.sleep(1)
	console.print('Sorting path:', args.path)
	time.sleep(1)
	for file in files:
		cTime = time.strftime('%I:%M:%S %p, %d/%m/%Y',time.localtime(os.path.getctime(os.path.join(args.path, file))))
		size = os.path.getsize(os.path.join(args.path, file))
		ext = os.path.splitext(file)
		if size == 0 or args.extension != ext[1]:  # Excludes files or folders showing 0KB from showing
			continue;
		elif size < 1024 * 1024: #If size < 1MB
			size_kb = size / 1024
			console.print(f'[{index}] File Name: [white]"{file}"[/white] - Date Created: {cTime} | Size: [white underline bold]{size_kb:.2f} KB')
			index += 1
		elif size < 1024 * 1024 * 1024:
			size_mb = size /  (1024 * 1024)
			console.print(f'[{index}] File Name: [yellow]"{file}"[/yellow] - Date Created: {cTime} | Size: [yellow underline bold]{size_mb:.2f} MB')
			index += 1
		else:
			size_gb = size / (1024 * 1024 * 1024)
			console.print(f'[{index}] File Name: [blue]"{file}"[/blue] - Date Created: {cTime} | Size: [blue underline bold]{size_gb:.2f} GB')
			index += 1

def fileSorter():
	index = 1;
	console.print('[red]No extension provided')
	time.sleep(1)
	console.print('Sorting path:', args.path)
	time.sleep(1)
	for file in files:
		cTime = time.strftime('%I:%M:%S %p, %d/%m/%Y',time.localtime(os.path.getctime(os.path.join(args.path, file))))
		size = os.path.getsize(os.path.join(args.path, file))
		if size == 0:  # Excludes files or folders showing 0KB from showing
			continue;
		elif size < 1024 * 1024: #If size < 1MB
			size_kb = size / 1024
			console.print(f'[{index}] File Name: [white]"{file}"[/white] - Date Created: {cTime} | Size: [white underline bold]{size_kb:.2f} KB')
			index += 1
		elif size < 1024 * 1024 * 1024:
			size_mb = size /  (1024 * 1024)
			console.print(f'[{index}] File Name: [yellow]"{file}"[/yellow] - Date Created: {cTime} | Size: [yellow underline bold]{size_mb:.2f} MB')
			index += 1
		else:
			size_gb = size / (1024 * 1024 * 1024)
			console.print(f'[{index}] File Name: [blue]"{file}"[/blue] - Date Created: {cTime} | Size: [blue underline bold]{size_gb:.2f} GB')
			index += 1

# if args.extension is None:
# 	fileSorter()
# else:
# 	extFileSorter()

file_to_array()
console.print("[green bold]Done sorting :smile:")