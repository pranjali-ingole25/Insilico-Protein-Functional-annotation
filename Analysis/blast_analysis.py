from Bio.Blast import NCBIWWW,NCBIXML
from Bio import SeqIO

record = SeqIO.read(r"D:\Biopython\Data\Sequence.fasta","fasta")

result_handle = NCBIWWW.qblast(
    program="blastp",
    database="nr",
    sequence=record.seq,
)

with open(r"D:\Biopython\Result\blast_results.xml", "w") as b:
    b.write(result_handle.read())

with open (r"D:\Biopython\Result\blast_results.xml") as b:
    blast_record = NCBIXML.read(b) 
    print(len(blast_record.alignments))

    for alignment in blast_record.alignments[:10]:
        for hsp in alignment.hsps:
            print("Hit title: ",alignment.title)
            print("Length: ",str(alignment.length))
            print("Score: ", str(hsp.score) )
            print("E-value: ", str(hsp.expect) )
            identity_percent = (hsp.identities / hsp.align_length) * 100
            print(f"Identities: {identity_percent:.2f}%")

            print("-" * 60 + "\n")


print("BLAST analysis completed.")