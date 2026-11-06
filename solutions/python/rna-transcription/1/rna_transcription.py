def to_rna(dna_strand):
    """
        Both DNA and RNA strands are a sequence of nucleotides.
        The four nucleotides found in DNA are adenine (A), cytosine (C), guanine (G), and thymine (T).
        The four nucleotides found in RNA are adenine (A), cytosine (C), guanine (G), and uracil (U).
        
        Given a DNA strand, its transcribed RNA strand is formed by replacing each nucleotide with its complement:
            G -> C
            C -> G
            T -> A
            A -> U 

        Parameters:
            dna_strand(str): String of nucleotide.

        Return:
            str: String of complement the nucleotide on given dna strand
    """
    complement = {"G": "C", "C": "G", "T": "A", "A": "U"}
    dna_strands = list(dna_strand)

    for strand_index, strand in enumerate(dna_strands):
        dna_strands[strand_index] = complement[strand]

    return "".join(dna_strands)
