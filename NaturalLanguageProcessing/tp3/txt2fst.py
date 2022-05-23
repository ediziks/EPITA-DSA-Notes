#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os

import fileinput

cpt=0
start=1;
f = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin    
for line in f:
    if len(line.strip()) > 0:
       for words in line.strip().split(' '):
         if (start == 1):
            print ("0\t"+str(cpt+1)+"\t"+words)
            start=0
         else:
            print (str(cpt)+"\t"+str(cpt+1)+"\t"+words)
            start=0
         cpt=cpt+1
       print (str(cpt))
       cpt=cpt+1
       start=1
    