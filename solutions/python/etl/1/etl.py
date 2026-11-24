def transform(legacy_data):
    lexiconia = {}

    for key, values in legacy_data.items():
        for letter in values:
            lexiconia[letter.lower()] = key

    sorted_lex = dict(sorted(lexiconia.items()))

    return sorted_lex