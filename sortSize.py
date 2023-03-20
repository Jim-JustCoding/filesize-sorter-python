#!/usr/bin/env python3

import os
import time
import argparse
from colorama import init as colorama_init
from colorama import Back
from colorama import Fore
from colorama import Style

# Accept an argument before execution
parser = argparse.ArgumentParser(description='Sort files based on their file size.')
parser.add_argument('path', metavar='path', type=str, help='the path to the directory')
args = parser.parse_args()

colorama_init()

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
		print(f'{Back.BLACK}[{index}] "{file}" - {cTime} |  {Style.BRIGHT}{size_kb:.2f} KB{Style.RESET_ALL}')
	elif size < 1024 * 1024 * 1024:
		size_mb = size /  (1024 * 1024)
		print(f'{Fore.YELLOW}[{index}] "{file}" - {cTime} |  {Style.BRIGHT}{size_mb:.2f} MB{Style.RESET_ALL}')
	else:
		print(f'{Fore.BLUE}[{index}] "{file}" - {cTime} |  {Style.BRIGHT}{size_gb:.2f} GB{Style.RESET_ALL}')
