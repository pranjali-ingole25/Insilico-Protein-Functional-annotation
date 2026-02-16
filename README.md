🧬 In-silico Identification and Functional Characterization of an Uncharacterized Protein

📌 Project Overview

This project focuses on the computational identification and functional annotation of an uncharacterized protein using sequence analysis and homology-based annotation.
The study demonstrates how an unknown biological sequence can be analyzed in silico to predict its quality, similarity, and biological function using Biopython and Bioinformatics Tools.


🧪 Dataset

Sequence source: UniProt

Protein ID: Q2W564

Description: Uncharacterized protein

Sequence format: FASTA


⚙️ Tools & Technologies Used

Python 3

Biopython

NCBI BLASTP

InterproScan

VS Code

Git & GitHub


🔬 Methodology / Pipeline

1️⃣ Sequence Retrieval

The protein sequence was retrieved from the UniProt database in FASTA format.

2️⃣ Sequence Quality Analysis & Validation

Basic quality checks were performed to assess the suitability of the sequence for functional prediction:
Sequence length calculation
Identification of unknown residues (X)
Amino acid composition analysis

3️⃣ Homology Search (BLAST Analysis)

BLASTP was performed against the NCBI non-redundant protein database using Biopython.

Key BLAST Parameters:

Database: nr

Program: BLASTP

4️⃣ Functional Annotation

Using BLAST homology and domain analysis (InterPro results), the protein was classified as an L,D-transpeptidase family protein.

Predicted Function:

Peptidoglycan cross-linking

Bacterial cell wall biosynthesis

Maintaining structural integrity of the cell wall

5️⃣ Biological Interpretation

The analyzed protein from Paramagnetospirillum magneticum strain AMB-1 was predicted to belong to the L,D-transpeptidase family based on homology and conserved domain analysis. L,D-transpeptidases are key enzymes involved in peptidoglycan cross-linking, contributing to bacterial cell wall maturation, structural stability, and environmental stress adaptation.

As a magnetotactic bacterium, P. magneticum inhabits dynamic aquatic environments and relies on robust cellular architecture to maintain morphology and support magnetosome formation. The presence of an L,D-transpeptidase suggests a role in cell wall remodeling and structural maintenance, which may indirectly support magnetosome organization and survival under fluctuating environmental conditions. Additionally, L,D-transpeptidases are associated with alternative peptidoglycan cross-linking pathways and may contribute to intrinsic antibiotic resistance mechanisms.

