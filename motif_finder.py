from Bio.Seq import Seq
dna=input(Seq("Enter DNA sequence:")).upper()
motif=input(Seq("Enter Motif:")).upper()
for i in range(len(dna)-len(motif)+1):
    if dna[i:i+len(motif)]==motif:
        print("Motif found at position:",i+1)
