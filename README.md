🧬 In-silico Identification and Functional Characterization of an Uncharacterized Protein
📌 Project Overview

This project focuses on the computational identification and functional annotation of an uncharacterized protein using sequence analysis and homology-based annotation.
The study demonstrates how an unknown biological sequence can be analyzed in silico to predict its quality, similarity, and biological function using Biopython and Blast.

🎯 Research Question

How can an unknown or hypothetical biological sequence be computationally analyzed to assess its quality, identify homologous sequences, and predict its biological function?

🧪 Dataset

Sequence source: UniProt

Protein ID: Q2W564

Description: Uncharacterized protein

Sequence format: FASTA

⚙️ Tools & Technologies Used

Python 3

Biopython

NCBI BLASTP

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

Validation based on sequence length threshold

Result:
The sequence length (~535 amino acids) and low number of unknown residues indicated that the sequence is suitable for downstream analysis.

3️⃣ Homology Search (BLAST Analysis)

BLASTP was performed against the NCBI non-redundant protein database using Biopython.

Key BLAST Parameters:

Database: nr

Program: BLASTP

📊 BLAST Results Summary
Parameter	Result
Top Hit	L,D-transpeptidase family protein
Organism	Paramagnetospirillum magneticum
Sequence Length	535 aa
Identity	100%
E-value	0.0

Multiple high-confidence homologs were identified across related magnetotactic bacteria, indicating strong evolutionary conservation.

🧠 Functional Annotation

Based on BLAST homology, the query protein was annotated as an L,D-transpeptidase family protein.

Predicted Function:

Involved in peptidoglycan cross-linking

Plays a role in bacterial cell wall biosynthesis

Contributes to cell wall stability and maintenance

🧬 Biological Interpretation

The high sequence identity and conservation across multiple bacterial species suggest that the protein performs an essential cellular function. L,D-transpeptidases are known to be critical for bacterial survival and structural integrity, and in some organisms, they are associated with antibiotic resistance mechanisms.

