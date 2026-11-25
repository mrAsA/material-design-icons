def sum_of_multiples(limit, multiples):

    mult_num = [num for num in range(1, limit) for item in multiples if item > 0 and num % item == 0]
    set_num = set(mult_num)

    return sum(set_num)
