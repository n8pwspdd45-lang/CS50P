# DNA to Protein Toolkit

A Python command-line toolkit for analyzing DNA sequences and coding sequences (CDS).
The program reads FASTA files, validates sequences, and performs a range of
bioinformatics operations: GC content calculation, *in silico* transcription to
pre-mRNA, reverse complement generation, motif search, and protein-level analysis
for CDS inputs (translation, molecular weight, instability index, isoelectric point).

The project was built as the final project for **CS50P – Introduction to Programming
with Python** and uses [Biopython](https://biopython.org/) for the biology-specific
operations.

---

## Background

The program distinguishes between two kinds of input, because they require
different analyses:

- **Genomic DNA** – the full sequence of a gene, including introns and
  non-coding regions. From this, the program computes GC content, produces the
  pre-mRNA (unspliced), and generates the reverse complement.
- **CDS (Coding Sequence)** – the mature, spliced sequence that is actually
  translated into protein. From this, the program derives the protein sequence
  and computes protein-level properties.

This separation is deliberate: **it is not possible to translate a whole genomic
sequence** into a meaningful protein, because the sequence contains introns and
non-coding regions. A real cell performs *splicing* to remove introns before
translation. This program **does not perform splicing *in silico*** — the user
must provide the CDS separately. This is a documented limitation, not an oversight.

---

## Features

### Genomic sequence analysis (`gDNA` class)

- **Input validation** – only A, T, G, C are accepted; anything else raises
  `ValueError` at object creation.
- **GC content** – percentage of G + C over the total length.
- **Transcription** – DNA → pre-mRNA (T replaced by U, no splicing).
- **Reverse complement** – the complementary strand, 5' → 3'.
- **FASTA output** – both pre-mRNA and reverse complement can be written to
  `.fasta` files.
- **Motif search** – finds all (possibly overlapping) occurrences of a motif,
  returning 0-based start positions.

### CDS analysis (`CDS` class, inherits from `gDNA`)

- **Translation** – CDS → protein, stopping at the first in-frame stop codon
  (`to_stop=True`).
- **Protein length** – number of amino acids.
- **Molecular weight** – in Dalton (Da).
- **Instability index** – values > 40 indicate a potentially unstable protein.
- **Isoelectric point (pI)** – theoretical pH at which the protein has no net
  charge.

### Custom functions (module level)

Three pure functions are defined at module level, as required by the CS50P
specification:

- `validate_dna_sequence(seq)` – returns `True` if the sequence contains only
  A, T, G, C (and is non-empty).
- `motif_finder(seq, motif)` – returns a list of 0-based start positions.
- `gc_content(seq)` – returns the GC percentage as a float.

These functions are pure (no I/O, no side effects) and are tested directly
with `pytest`.

---

## Project Structure

```text
project/
├── project.py
├── test_project.py
├── requirements.txt
└── README.md
```

---

## Installation

1. Clone the repository (or download the files).
2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Run the program:
```bash
python project.py
```
You will be asked whether to analyze a genomic sequence (g) or a CDS (c).

### Example: genomic sequence

```
Do you want to analyze a genomic sequence (g) or a CDS (c)? g
Enter the path to the FASTA file of the genomic sequence: GAPDH_genomic.fasta
%GC: 60.10%
Find pre_mRNA seq to premRNA_ENST00001137778.1.fasta
Note: the input DNA sequence was treated as the coding (sense) strand.
Find reverse complement to reverse_complement_ENST00001137778.1.fasta
Do you want to find a motif (y/n)? y
Enter the motif to search for: ATG
Motif 'ATG' found at 67 position(s) (overlapping): [176, 243, ...]
```

### Example: CDS

```
Do you want to analyze a genomic sequence (g) or a CDS (c)? c
Enter the path to the FASTA file of the CDS: GAPDH_cds.fasta
Protein: MGKVKVGVNGFGRIGRLVTRAAFNSGKVDIVA...
Protein length (AA): 335
Molecular weight of the protein in ENST00001137778.1: 36052.79 Da
The protein's instability index is: 15.61
The protein's isoelectric point is: 8.57
```

### Input requirements

- The input must be a **valid FASTA file** with **exactly one record**. Multi-record files are rejected (`SeqIO.read` requires a single record).
- The sequence must contain only A, T, G, C (case-insensitive). Sequences with `N` (undetermined bases) or IUPAC ambiguity codes are rejected.
- The CDS must be provided as a **separate FASTA file** — the program does not
perform splicing.

---

## Design decisions

A few choices were made deliberately and are worth explaining:
1. **Validation in the constructor**.
  A `gDNA` object cannot exist if its sequence is invalid. The check is performed once, in `__init__`, and raises `ValueError` before the object is fully created. This means every `gDNA` instance is guaranteed to be valid, and no other method needs to re-check.
2. **Pure functions + thin class methods**
  The core logic (`validate_dna_sequence`, `motif_finder`, `gc_content`) lives in pure module-level functions. The class methods are thin wrappers that delegate to those functions. This keeps the logic testable in isolation and satisfies the CS50P requirement of three custom functions at module level.
3. **Separation of computation and I/O**.
  Methods like `transcription()` and `reverse_complement()` return values; methods like `write_premRNA_fasta()` handle file I/O. The program never mixes computation and printing inside the classes.
4. `to_stop=True` **for translation**.
  The protein sequence stops at the first in-frame stop codon, and the stop symbol (`*`) is omitted. This produces the mature protein sequence, which is what a user typically wants to see.
5. **CDS separate from genomic input**.
  As explained in Background, the program does not perform splicing. The user must supply the CDS as a separate FASTA file.

---

## Limitations

This project is intentionally scoped. The following are **known limitations**, documented honestly:

- **No splicing *in silico***. The program cannot derive a CDS from a genomic sequence. The user must provide the CDS separately. Implementing a splicing algorithm (exon/intron detection) is beyond the scope of this project.
- **No IUPAC ambiguity codes**. Only A, T, G, C are accepted. Sequences containing N, R, Y, etc. are rejected.
- **Single-record FASTA only**. `SeqIO.read` requires exactly one record per file Multi-record files (e.g. whole chromosomes) are rejected.
- **No alignment or BLAST**. The program does not compare sequences against databases or perform pairwise alignment.
- **No database lookups**. Transcript/protein names are not retrieved from Ensembl or other databases; the program works entirely offline.
- **Motif search is exact-match only**. No degenerate motifs, no position weight matrices.
- **Protein properties are theoretical**. Molecular weight, instability index, and pI are computed from the sequence, not measured experimentally.

**These limitations are deliberate**: the goal was a focused, well-tested toolkit,
not a full-fledged bioinformatics pipeline.

---

## Testing

The test suite uses `pytest` and covers both the module-level functions and the class methods:
  ```bash
  pytest test_project.py -v
  ```
The suite includes:
- **Validation tests** – valid, invalid, empty, lowercase sequences.
- **Motif tests** – found, not found, overlapping occurrences.
- **GC content tests** – all-GC, mixed, no-GC sequences.
- **Transcription and reverse complement tests** – known inputs and outputs.
- **Translation tests** – a known CDS and its expected protein.
- **Protein property tests** – molecular weight, instability index, and pI compared against reference values from [ProtParam](https://web.expasy.org/protparam/) using `pytest.approx`.

---

## Author

Matilde Luce Baraldi
Second-year student in Medical Biotechnology, University of Milan (Unimi).
Final project for CS50P.


