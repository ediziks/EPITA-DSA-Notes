#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os

import fileinput

#for line in fileinput.input():
    #pass

#for arg in sys.argv: ￼
    #print arg
    
#if not os.path.exists(sys.argv[0])
    #print "Error file does not exists "
cpt=0
print("<eps> "+str(cpt))
f = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin    
for line in f:
    if len(line.strip()) > 0:
        cpt=cpt+1
        print(line.strip()+" "+str(cpt))
    
    
