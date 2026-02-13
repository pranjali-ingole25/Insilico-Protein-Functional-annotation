from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis

record = SeqIO.read("D:\Biopython\Data\Sequence.fasta","fasta")


analysis = ProteinAnalysis(record)

print("Protein ID:", record.id)
print("Length:", len(record), "aa")

aa_count = analysis.count_amino_acids()
aa_percent = analysis.get_amino_acids_percent()

print("Amino Acid Count:")
for aa, count in aa_count.items():
    print(f"{aa}: {count : .2f}")

print("Amino Acid Composition (%):")
for aa, percent in aa_percent.items():
    print(f"{aa}: {percent*100: .2f} {"%"}")

print("Molecular Weight:", analysis.molecular_weight())
print("Isoelectric Point (pI):", analysis.isoelectric_point())
print("Instability Index:", analysis.instability_index())
print("Aromaticity:", analysis.aromaticity())
print("GRAVY:", analysis.gravy())
