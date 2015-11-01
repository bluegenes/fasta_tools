#!/usr/bin/env python

###################################################################
"""Function: Take in a FASTA file and a list of contig names: print
two fastas: one containing the fasta entries for contigs in the list; 
the other containing the remaining contigs in the input FASTA.
"""
###################################################################

import sys

contigNames = open(sys.argv[2], 'r')
basename = (sys.argv[1]).split('.fa')[0]
inList= open(basename + '_inList.fa', 'w')
notInList= open(basename + '_notInList.fa', 'w')

contigSet = set( [ x.strip() for x in contigNames ])

nameInList = False
with open(sys.argv[1], 'r') as f:
    for line in f:
        if line.startswith('>'):
	    name = line.rstrip().split(' ')[0][1:] #salmon names are abbreviated --> stop at first space
	    if name in contigSet:
		nameInList = True
	        inList.write(line)
	    else:
		nameInList=False
	        notInList.write(line)
	else:
	    if nameInList:
	        inList.write(line)
	    else:
	        notInList.write(line)

    f.close()

inList.close()
notInList.close()



