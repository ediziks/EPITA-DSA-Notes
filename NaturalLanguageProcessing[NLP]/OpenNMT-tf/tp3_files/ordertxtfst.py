#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os

import fileinput

cpt=0
start=1;
runfst={};
arcstart=0;
f = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin    
for line in f:
    if len(line.strip()) > 0:
       linefst=[]
       for words in line.strip().split('\t'):
         if (start == 1):
            arcstart=words;
            start=0
         linefst.append(words)
       runfst[linefst[0]]=linefst

tmplist=[]
while (arcstart != -1):
  tmplist=runfst[arcstart]
  if len(tmplist) > 2:
    print (tmplist[2]+"\t"+tmplist[3]+"\t"+tmplist[4])
    arcstart=tmplist[1]
  else:
    arcstart = -1
