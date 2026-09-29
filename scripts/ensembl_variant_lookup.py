"""Retrieve public Ensembl variation information for a variant identifier.

Default variant reflects the identifier discussed in the archived coursework report.
Internet access is required.
"""
import argparse, json, requests

def main():
    p=argparse.ArgumentParser(); p.add_argument('variant',nargs='?',default='rs1057519777'); args=p.parse_args()
    url=f'https://rest.ensembl.org/variation/human/{args.variant}'
    r=requests.get(url,headers={'Content-Type':'application/json'},timeout=30); r.raise_for_status()
    print(json.dumps(r.json(),indent=2))
if __name__=='__main__': main()
