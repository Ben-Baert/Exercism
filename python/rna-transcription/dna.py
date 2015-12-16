TO_RNA = str.maketrans({"C" : "G", "G" : "C", "T" : "A", "A" : "U"})

def to_rna(dna):
    return dna.translate(TO_RNA)