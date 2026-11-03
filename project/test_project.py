import pytest
from project import gDNA, CDS, validate_dna_sequence, motif_finder, gc_content

# Test for custom functions in project
def test_validate_dna_sequence_valid():
    assert validate_dna_sequence("ATGC") is True

def test_validate_dna_sequence_invalid_char():
    assert validate_dna_sequence("ATXC") is False

def test_validate_dna_sequence_empty():
    assert validate_dna_sequence("") is False

def test_validate_dna_sequence_lowercase():
    assert validate_dna_sequence("atgc") is True

def test_motif_finder():
    assert motif_finder("GGGCCG", "CCG") == [3]

def test_gc_content_all_gc():
    assert gc_content("GGGCCG") == 100.0

def test_gc_content_mixed():
    assert gc_content("GGCATTGCCA") == 60.0

def test_gc_content_no_gc():
    assert gc_content("AAAATTAT") == 0.0



# Test for DNA toolkit
def test_invalid_sequence_raises():
    with pytest.raises(ValueError):
        gDNA("GGGCCGNNXAAATAGGGAGATCC", "test")

def test_valid_sequence_doesnt_raises():
    dna = gDNA("GGGCCG", "test")
    assert dna.seq == "GGGCCG"


def test_transcription():
    dna = gDNA("GGGCCGAT", "test")
    rna = dna.transcription()
    assert rna == "GGGCCGAU"

def test_reverse_complement():
    dna = gDNA("GGGCCGAAATAGGGAGATCC", "test")
    rc = dna.reverse_complement()
    assert rc == "GGATCTCCCTATTTCGGCCC"


# Test for protein sequence analyzer
def test_translate():
    seq = CDS("ATGAGGATCACTAGGTAA", "test")
    protein = seq.translate()
    assert protein == "MRITR"

def test_protein_lenght():
    seq = CDS("ATGAGGATCACTAGGTAA", "test")
    lenght = seq.protein_lenght()
    assert lenght == 5

def test_molecular_weight():
    seq = CDS("ATGAGGATCACTAGGTAA", "test")
    weight = seq.molecular_weight()
    assert weight == pytest.approx(675.85, rel=0.01)

def test_instability_index():
    seq = CDS("ATGAGGATCACTAGGTAA", "test")
    ii = seq.instability_index()
    assert ii == pytest.approx(-7.08, abs=0.1)

def test_isoelectric_point():
    seq = CDS("ATGAGGATCACTAGGTAA", "test")
    pI = seq.isoelectric_point()
    assert pI == pytest.approx(12.00, abs=0.1)
