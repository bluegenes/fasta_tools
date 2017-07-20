#Tessa Pierce
# 2.8.13


#Input - fasta file
#Output - basic BED file ( chr_name + '\t' + start_pos + '\t' + end_pos )


import sys, re

in_fasta = open(sys.argv[1], 'r')
out_BED = open(sys.argv[2], 'w')


fasta_lines = in_fasta.readlines()

#info = re.compile('^>(\S*)') #cegma
info = re.compile('^>(\S*) len=(\d*)') #trinity
#info = re.compile('^>(\S*) (\d*)') #velvet-oases
start_pos = str(0) # BED files: start is 0-indexed, end is 1-indexed

for line in fasta_lines:
    contig_info = info.match(line)
    if contig_info is not None:
        contig_name, end_pos = contig_info.groups()
        out_BED.write(contig_name+ '\t' + start_pos + '\t' + end_pos + '\n')	
        #out_BED.write(contig_name + '\t' + end_pos + '\n')	# bed for genomeCov
    

in_fasta.close()
out_BED.close()

sys.exit()





