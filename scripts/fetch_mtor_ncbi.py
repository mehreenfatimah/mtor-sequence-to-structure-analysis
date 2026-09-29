"""Fetch public human MTOR records from NCBI E-utilities.

Usage: python scripts/fetch_mtor_ncbi.py
Internet access is required.
"""
from pathlib import Path
from urllib.request import urlopen

OUT=Path(__file__).resolve().parents[1]/'data'/'downloaded'
OUT.mkdir(parents=True,exist_ok=True)
GENE_ID='2475'

def fetch(url):
    with urlopen(url,timeout=30) as r: return r.read()

def main():
    summary=fetch(f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=gene&id={GENE_ID}&retmode=json')
    (OUT/'ncbi_gene_2475_summary.json').write_bytes(summary)
    # RefSeq genomic/sequence choice can change; the gene summary is retained as the stable identifier source.
    print(f'Wrote public NCBI Gene summary for MTOR (Gene ID {GENE_ID}) to {OUT}')

if __name__=='__main__': main()
