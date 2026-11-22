def distance(strand_a, strand_b):

    hamming_distance = 0
    list_strand_a = list(strand_a)
    list_strand_b = list(strand_b)
    
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")


    for index_strand, strand in enumerate(list_strand_a):
        if strand != list_strand_b[index_strand]:
            hamming_distance += 1

    return hamming_distance
