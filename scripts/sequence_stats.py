"""Compute simple nucleotide/protein sequence statistics for FASTA input."""
from pathlib import Path
import argparse
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

def main():
    p=argparse.ArgumentParser(); p.add_argument('fasta'); args=p.parse_args()
    for rec in SeqIO.parse(args.fasta,'fasta'):
        seq=str(rec.seq).upper()
        print(f'{rec.id}\tlength={len(seq)}\tGC={gc_fraction(seq)*100:.2f}%')
if __name__=='__main__': main()
