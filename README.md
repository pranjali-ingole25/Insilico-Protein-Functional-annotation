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

High sequence identity and conservation across species suggest an essential cellular function.
L,D-transpeptidases are critical for bacterial survival and, in some cases, linked to antibiotic resistance mechanisms.
Insights from this analysis can guide experimental validation or further bioinformatics studies on uncharacterized proteins.

