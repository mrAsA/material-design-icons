def find_anagrams(word, candidates):
    reorder_word = "".join(sorted(word.lower()))
    #anagrams = []

    anagrams = [candidate for candidate in candidates if reorder_word == "".join(sorted(candidate.lower())) and word.lower() != candidate.lower()]
    #for candidate in candidates:
    #    reorder_candidate = "".join(sorted(candidate.lower()))

    #    if reorder_word == reorder_candidate and word.lower() != candidate.lower():
    #       anagrams.append(candidate)

    return anagrams
