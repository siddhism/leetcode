def get_ugly_number(n):
    ugly = [0 for i in range(n+1)]
    i2 , i3 , i5 = 0, 0, 0
    next_multiple_of_2, next_multiple_of_3, next_multiple_of_5 = 1, 1, 1

    for i in range(1, n+1):
        next_ugly_no = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)
        ugly[i] = next_ugly_no

        if (next_ugly_no == next_multiple_of_2):
            i2 = i2 + 1
            next_multiple_of_2 = ugly[i2] * 2
        if (next_ugly_no == next_multiple_of_3):
            i3 = i3 + 1
            next_multiple_of_3 = ugly[i3] * 3
        if (next_ugly_no == next_multiple_of_5):
            i5 = i5 + 1
            next_multiple_of_5 = ugly[i5] * 5
    return ugly[n]

n = 150
print get_ugly_number(7)
print get_ugly_number(10)
print get_ugly_number(15)
print get_ugly_number(150)
