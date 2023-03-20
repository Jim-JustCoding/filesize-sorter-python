#!/usr/bin/env python3

import os
import time
import argparse
from rich import print
from rich.style import Style
from console import console

# Accept an argument before execution
parser = argparse.ArgumentParser(description='Sort files based on their file size.')
parser.add_argument('path', metavar='path', type=str, help='the path to the directory')
args = parser.parse_args()

#Get list of all files and directories from the argument
files = os.listdir(args.path)
files.sort(key=lambda x: os.path.getsize(os.path.join(args.path, x)))

def fileSorter():
	index = 0;
	for file in files:
		cTime = time.strftime('%I:%M:%S %p, %d/%m/%Y',time.localtime(os.path.getctime(os.path.join(args.path, file))))
		size = os.path.getsize(os.path.join(args.path, file))
		size_gb = size / (1024 * 1024 * 1024)
		if size == 0: # Excludes files or folders showing 0KB from showing
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
			console.print(f'[{index}] File Name: [blue]"{file}"[/blue] - Date Created: {cTime} | Size: [blue underline bold]{size_gb:.2f} GB')
			index += 1
			if index == 126:
				open(os.path.join(args.path, file))

fileSorter()
console.print("[green bold]Done sorting :smile:")