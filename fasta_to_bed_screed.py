#Tessa Pierce

#Input - fasta file
#Output - basic BED file ( chr_name + '\t' + start_pos + '\t' + end_pos )

import argparse
import screed

def fasta_to_bed(in_fasta,out_bed):
    if not out_bed:
        out_bed = in_fasta.split('.fa')[0] + '.bed'
    with screed.open(in_fasta) as seqF:
        with open(out_bed, 'w') as out:
            for read in seqF:
                out.write('\t'.join([read.name, '0', str(len(read.sequence))]) + '\n')

if(__name__=='__main__'):
    parser = argparse.ArgumentParser(description="Create simple BED from fasta")
    parser.add_argument('--fasta', help='input fasta file')
    parser.add_argument('--bed', help='output bed file')
    args = parser.parse_args()
    fasta_to_bed(args.fasta,args.bed)
