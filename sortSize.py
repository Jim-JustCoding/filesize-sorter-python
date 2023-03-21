#!/usr/bin/env python3

import os
import time
import argparse
from filesize_converter import *
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

# Ask user for sort order. If an input other than A or D is given, order will default to ascending
def userInput():
	console.print("[yellow]Press A for Ascending Order, or D for Descending Order")
	global input 
	input = str(input(""))
	orderInput()

def orderInput(): 
	if input.lower() in ('a', 'ascending', 'asc'): #Although program asks for 'A' or 'D', input's less strict
		console.print("[cyan bold]The files will be sorted in ascending order")
		time.sleep(1)
		return
	if input.lower() in ('d', 'descending', 'desc'):
		console.print("[cyan bold]The files will be sorted in descending order")
		time.sleep(1)
		files.reverse();
		return
	else:
		console.print("[red]Input Unknown. Defaulting to ascending")
		time.sleep(1)

#Checks if --extension is a known file extension from filename_extensions.txt before continuing on. Otherwise, quit the program
def ext_checker():
	with open("filename_extensions.txt", 'r') as f:
		lines = f.read().splitlines()
		for l in lines:
			if l == args.extension:
				console.log(l)
				console.log('Found extension')
				time.sleep(1)
				extFileSorter()
				break
		if l != args.extension:
			console.print("[red bold]The", args.extension, "[red bold]Extension does not exist. Closing program...")
			quit()
				
#Filter by given --extension only. 
def extFileSorter():
	console.print('[green]Extension to filter:', args.extension)
	time.sleep(1)
	fileConverter()

#Sorts every file in given directory
def fileSorter():
	console.print('[red]No extension provided')
	time.sleep(1)
	fileConverter()

def fileConverter():
	index = 1
	counter = 0
	console.print('Sorting path:', args.path)
	time.sleep(1)
	total_size = 0
	for file in files:
		cTime = time.strftime('%I:%M:%S %p, %d/%m/%Y',time.localtime(os.path.getctime(os.path.join(args.path, file))))
		size = os.path.getsize(os.path.join(args.path, file))
		ext = os.path.splitext(file)
		if size == 0:  # Excludes files or folders showing 0KB
			continue
		if args.extension != None and args.extension != ext[1]: # If extension was provided, filter by given --extension only
			continue
		if size < 1024 * 1024: #If size < 1MB
			size_kb = calcSize(size)
			if file in ext: #Dims any 'folders' found during the sort operation
				console.print(f'[{index}] [dim white]Folder Name: "{file}"[/dim white] - Date Created: {cTime} | Size: [white underline bold]{size_kb}', '\n')
			else:
				console.print(f'[{index}] File Name: [white]"{file}"[/white] - Date Created: {cTime} | Size: [white underline bold]{size_kb}', '\n')
			index += 1
			counter += 1
		elif size < 1024 * 1024 * 1024: #If size <1GB and >1MB
			size_mb = calcSize(size)
			console.print(f'[{index}] File Name: [yellow]"{file}"[/yellow] - Date Created: {cTime} | Size: [yellow underline bold]{size_mb}', '\n')
			index += 1
			counter += 1
		else: # Size > 1GB
			size_gb = calcSize(size)
			console.print(f'[{index}] File Name: [blue]"{file}"[/blue] - Date Created: {cTime} | Size: [blue underline bold]{size_gb}', '\n')
			index += 1
			counter += 1
		total_size += size
	if counter == 0:
		console.print("[red bold]There are either no files in this directory, or no files were found with your given extension.")
		quit()
	else:
		console.print("[white on green]Files found:", counter)
		console.print("[green bold]Done sorting :smile:")
		console.print("Total Files:", calcSize(total_size))
		console.print(total_size, "bytes")
		if (total_size > 5368709120):
			console.print("Uh oh. Might wanna do some housekeeping with your files, there")
		quit()

userInput()
if args.extension is None:
	fileSorter()
else:
	ext_checker()