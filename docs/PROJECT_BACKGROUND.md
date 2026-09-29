# Project background

## Academic context

This project originated as BIO310 undergraduate coursework titled **“Comprehensive Bioinformatics Analysis of a Gene: From Sequence to Structure.”** The human **MTOR** gene (NCBI Gene ID **2475**) was used as the case study.

## Original analysis scope

The coursework documented a multi-stage, tool-assisted bioinformatics analysis involving:

1. NCBI Gene and Ensembl retrieval/cross-checking
2. BLAST homology exploration
3. Ensembl Variant Effect Predictor (VEP)
4. cross-species multiple-sequence alignment and phylogenetic analysis in MEGA
5. RNA secondary-structure exploration using RNAfold
6. protein-structure inspection using SWISS-MODEL and AlphaFold resources
7. pathway and functional interpretation using KEGG and Reactome

The work was primarily completed through public databases and interactive bioinformatics tools, with results recorded in the academic report and screenshots.

## GitHub version

This repository organizes the project into a cleaner technical format suitable for a public portfolio. A small set of scripts was added later for current public-record retrieval and basic sequence statistics:

- `fetch_mtor_ncbi.py`
- `ensembl_variant_lookup.py`
- `sequence_stats.py`

These scripts support the project but should not be confused with the complete original workflow. Stages that originally relied on interactive tools remain described as methodology unless their original machine-readable outputs are available.

## Variant interpretation note

The archived coursework discusses `rs1057519777`. Variant annotations can change as databases and evidence are updated. The included Ensembl lookup script queries the current public record rather than hard-coding an old interpretation as permanent fact.

## Scientific scope

This repository is intended to demonstrate undergraduate bioinformatics analysis, use of biological databases, sequence/variant/structure concepts, and scientific interpretation. It is **not** intended for clinical diagnosis or medical decision-making.


## Original analysis evidence

Selected figures from the original analysis are included in `results/` for easier review.
