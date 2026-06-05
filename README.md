# DNA Motif Finder 🧬

A Python-based bioinformatics tool that identifies specific DNA motifs within a DNA sequence and reports their positions.

## Features

- Search for a user-defined DNA motif
- Find all motif positions in a DNA sequence
- Case-insensitive input handling
- Simple and beginner-friendly implementation

## Technologies Used

- Python

## How It Works

The program:

1. Takes a DNA sequence as input
2. Takes a motif (pattern) as input
3. Scans the DNA sequence using a sliding window approach
4. Compares each substring with the motif
5. Displays the positions where the motif is found

## Code

```python
dna = input("Enter DNA sequence: ").upper()
motif = input("Enter motif: ").upper()

for i in range(len(dna) - len(motif) + 1):
    if dna[i:i+len(motif)] == motif:
        print("Motif found at position:", i + 1)
```

## Example

Input:

```
Enter DNA sequence: ATGCGATGAAATG
Enter motif: ATG
```

Output:

```
Motif found at position: 1
Motif found at position: 6
Motif found at position: 11
```

## Bioinformatics Application

Motif finding is commonly used in bioinformatics to identify:

- Regulatory elements
- Protein binding sites
- Conserved DNA regions
- Functional sequence patterns

## Future Improvements

- FASTA file support
- Motif occurrence counter
- Multiple sequence analysis
- Graphical user interface (GUI)

## Author

Omkar Desai
