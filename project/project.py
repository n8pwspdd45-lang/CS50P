from Bio.SeqUtils.ProtParam import ProteinAnalysis
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio import SeqIO
import sys


def motif_finder(seq, motif):
        positions = []
        start=0
        while True:
            pos = seq.find(motif, start)
            if pos == -1:
                break
            positions.append(pos)
            start = pos + 1
        return positions


def validate_dna_sequence(seq):
    if not seq:
        return False
    return all(n in "ATGC" for n in seq.upper())


def gc_content(seq):
    if not seq:
        return 0.0
    return (seq.count("G") + seq.count("C")) / len(seq) * 100


class gDNA:
    def __init__(self, seq, id):
        self.seq = str(seq).upper()
        self.id = id
        if not validate_dna_sequence(self.seq):
            raise ValueError(f"Invalid DNA sequence for {id}: only A, T, G, C allowed.")

    def transcription(self):
        return Seq(self.seq).transcribe()

    def write_premRNA_fasta(self, output_fasta_rna):
        pre_mRNA_record = SeqRecord(self.transcription(), id=self.id + "_premRNA", description="")
        SeqIO.write(pre_mRNA_record, output_fasta_rna, "fasta")
        return output_fasta_rna

    def reverse_complement(self):
        return Seq(self.seq).reverse_complement()

    def write_reversecomplement_fasta(self, output_fasta_rc):
        reverse_complement_record = SeqRecord(self.reverse_complement(), id=self.id + "_reverse_complement", description="")
        SeqIO.write(reverse_complement_record, output_fasta_rc, "fasta")
        return output_fasta_rc


class CDS(gDNA):
    def translate(self):
        protein = str(Seq(self.seq).translate(to_stop=True))
        return protein

    def protein_lenght(self):
        return len(self.translate())

    def protein_analysis_obj(self):
        return ProteinAnalysis(self.translate())

    def molecular_weight(self):
        return self.protein_analysis_obj().molecular_weight()

    def instability_index(self):
        return self.protein_analysis_obj().instability_index()

    def isoelectric_point(self):
        return self.protein_analysis_obj().isoelectric_point()


def main():
    while True:
        seq_type = input("Do you want to analyze a genomic sequence (g) or a CDS (c)? ").lower()
        if seq_type == "g":
            analyze_genomic_seq()
            break
        elif seq_type == "c":
            analyze_cds_seq()
            break
        else:
            print("Invalid choice. Please enter 'g' or 'c'.")


def analyze_genomic_seq():
    # Get genomic sequence from FASTA file and create a DNA object if the sequence is valid
    gen_path = input("Enter the path to the FASTA file of the genomic sequence: ")
    if not gen_path:
        sys.exit("No path provided.")

    try:
        record = SeqIO.read(gen_path, "fasta")
    except FileNotFoundError:
        sys.exit(f"File not found at {gen_path}")
    except ValueError as e:
        sys.exit(f"Invalid FASTA file: {e}")

    gen_seq = gDNA(record.seq, record.id)

    # Calculate GC content
    print (f"%GC: {gc_content(gen_seq.seq):.2f}%")

    # Create a file with pre_mRNA sequence
    path_mRNA = gen_seq.write_premRNA_fasta(f"premRNA_{record.id}.fasta")
    print (f"Find pre_mRNA seq to {path_mRNA}")
    print("Note: the input DNA sequence was treated as the coding (sense) strand.")

    # Create a file with reverse complement sequence
    path_rc = gen_seq.write_reversecomplement_fasta(f"reverse_complement_{record.id}.fasta")
    print (f"Find reverse complement to {path_rc}")

    # Motif finder (optional)
    while True:
        answer = input("Do you want to find a motif (y/n)? ").lower()
        if  answer == "y":
            motif = input("Enter the motif to search for: ").strip().upper()
            if all(n in "ATCG" for n in motif):
                positions = motif_finder(gen_seq.seq, motif)
                if positions:
                    print(f"Motif '{motif}' found at {len(positions)} position(s) (overlapping): {positions}")
                else:
                    print(f"Motif '{motif}' not found.")
            else:
                print("Invalid motif. Only A, T, G, C allowed.")
            break
        elif answer == "n":
            print("Analysis completed.")
            break
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")


def analyze_cds_seq():
    # Get cds sequence from FASTA file and create a CDS object
    cds_path = input("Enter the path to the FASTA file of the CDS: ")
    if not cds_path:
        sys.exit("No path provided.")

    try:
        record = SeqIO.read(cds_path, "fasta")
    except FileNotFoundError:
        sys.exit(f"File not found at {cds_path}")
    except ValueError as e:
        sys.exit(f"Invalid FASTA file: {e}")

    cds = CDS(record.seq, record.id)

    # Translate into protein and get protein lenght
    print(f"Protein: {cds.translate()}")
    print(f"Protein lenght (AA): {cds.protein_lenght()}")

    # Calculate molecular weight
    print(f"Molecular weight of the protein in {record.id}: {cds.molecular_weight():.2f} Da")

    # Calculate instability index
    print(f"The protein's instability index is: {cds.instability_index():.2f}")

    # Calculate isoelectric point
    print(f"The protein's isolectric point is: {cds.isoelectric_point():.2f}")



if __name__ == "__main__":
    main()
