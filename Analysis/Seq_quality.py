from Bio import SeqIO

record = SeqIO.read("D:\Biopython\Data\Sequence.fasta","fasta")

print("Sequence ID: ",record.id)    
print("Sequence Description: ",record.description)
print("Sequence: ",record.seq)

#Amino Acid Composition
amino_acids = "ACDEFGHIKLMNPQRSTVWY"
print("Amino acid composition:")
for aa in amino_acids:
    print(aa, ":", record.count(aa)) 

#Unknown residues
unknown_residues = record.count("X")
print("Unknown residues (X):", unknown_residues)

#Length validation
length = len(record)
print("Length of Sequence",len(record.seq))
if length < 100:
    print("Sequence too short for functional prediction")
elif unknown_residues > 2:
    print("Too many unknown residues")
else:
    print("Sequence length is suitable for analysis")


