def square_root(number):
    
    # running a loop base on whole number from 1 to number would be a disaster.
    # is the answer is within the lower half of number?
    # number = 25. 25 // 2 = 12, the 25 ** 0.5 is 5 and within 12
    # 196. 196 // 2 = 98. large one because the sqr is 14

    min, mid, max, = 1, 0, number // 2
    
    while min <= max:
        mid = (min + max) // 2
        sq = mid * mid
        
        if sq == number:
            return mid
        elif sq > number:
            max = mid - 1
        else:
            min = mid + 1

    return 1
        