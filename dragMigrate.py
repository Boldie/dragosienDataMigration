#! /usr/bin/python3

import argparse

parser = argparse.ArgumentParser(description='Migrates the data from Greasemonkey to Violentmonkey for Dragosien Resourceindikatoren')
parser.add_argument('--inFile', default="violentmonkey",
                    help='Input template file as from the violentmonkey export')
parser.add_argument('--outFile', default="violentmonkey",
                    help='Output file for violentmonkey import (may be same as in)')
parser.add_argument('--db', default="Dragosien_Resourcenindikatoren.db",
                    help='Database file from greasemonkey')

args = parser.parse_args()

import sqlite3
conn = sqlite3.connect(args.db)

import json

with open(args.inFile) as in_file:    
    data = json.load(in_file)

for row in conn.execute('SELECT * FROM scriptvals'):
    print("Working on value %s" % row[0])
    data["values"]["http%3A//serv.endoftheinternet.org/dragosien:Dragosien%20Resourcenindikatoren:"][row[0]]="s%s"%row[1].replace('\\"','"')[1:-1]

with open(args.outFile, 'w') as of:
    json.dump(data, of)

print("Modified file written to %s"%args.outFile)

import code
code.interact(local=locals())





