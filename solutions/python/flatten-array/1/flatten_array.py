def flatten(iterable):
    flat_iterable = []
    
    for item in iterable:
        if type(item) is list:
            flat_iterable.extend(flatten(item))
        else:
            if item is not None:
                flat_iterable.append(item)

    
    return flat_iterable