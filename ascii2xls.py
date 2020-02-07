#!/usr/bin/python3

import sys
if len(sys.argv) == 1:
	print ("Usage:", sys.argv[0], "SRC_PSEUDO_TABLE_FILE [DST_CSV_FILE]")
	exit()


from importlib import import_module
deps = ["bs4", "docutils", "dashtable", "pandas", "openpyxl", "xlwt"]
not_found = []

for dep in deps:
	try:
		import_module(dep)
	except:
		not_found.append(dep) 

if len(not_found) > 0:
	print("Required modules are not installed. Please install: ", ' '.join(not_found))
	exit()

args_cnt = len(sys.argv)
if args_cnt == 2:
	dst = sys.argv[1] + ".xlsx"
elif args_cnt == 3:
	dst = sys.argv[2]
else:
	print("2 arguments expected at most,", args_cnt, "given.")
	exit()

import dashtable as dt
import pandas as pd

try:
	text = open(sys.argv[1], 'r').read()
except:
	print("Unable to read file:", sys.argv[1])
	exit()

text = text\
.replace("┌","+").replace("┬","+").replace("┐","+")\
.replace("├","+").replace("┼","+").replace("┤","+")\
.replace("└","+").replace("┴","+").replace("┘","+")\
.replace("│","|").replace("─","-")

	
table, spans, use_headers = dt.grid2data(text)
frame = pd.DataFrame(table[1:], columns=table[0])
if dst[-4:] == ".csv":
	frame.to_csv(dst, index=False)
else:
	frame.to_excel(dst, index=False)


