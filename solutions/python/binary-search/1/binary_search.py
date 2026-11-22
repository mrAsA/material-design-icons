def find(search_list, value):
    index_val, min_val = 0, 0
    max_val = len(search_list) - 1

    while min_val <= max_val:
        middle = (min_val + max_val) // 2
        
        if search_list[middle] == value:
            return middle
        elif search_list[middle] < value:
            min_val = middle + 1
        else:
            max_val = middle - 1

    raise ValueError("value not in array")