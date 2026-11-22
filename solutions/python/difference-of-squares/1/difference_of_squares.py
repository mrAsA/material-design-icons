def square_of_sum(number):
    sum_num = 0
    for num in range(1, number + 1):
        sum_num += num

    return sum_num ** 2

def sum_of_squares(number):
    sum_sq = 0
    for num in range(1, number + 1):
        sum_sq += num ** 2

    return sum_sq

def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
