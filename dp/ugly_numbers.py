uglies = {}

def max_divide(a, b):
    original_num = a
    while a % b == 0:
        a = a / b
        cached_result = uglies.get(num)
        if cached_result:
            uglies[original_num] = True
            return True
    if a == 1:
        uglies[original_num] = True
    return False

def is_ugly(num):
    ugly = False
    original_num = num
    max_divide(num, 5)
    max_divide(num, 3)
    max_divide(num, 2)
    while num % 5 == 0:
        num = num /  5
        cached_result = uglies.get(num)
        if cached_result:
            uglies[original_num] = True
            return True
    while num % 3 == 0:
        num = num / 3
        cached_result = uglies.get(num)
        if cached_result:
            uglies[original_num] = True
            return True
    while num % 2 == 0:
        num = num / 2
        cached_result = uglies.get(num)
        if cached_result:
            uglies[original_num] = True
            return True
    if num == 1:
        ugly = True
    if ugly:
        uglies[num] = ugly
    return ugly

def get_n_th_ugly_no(n):

# TODO : handle condition where uglies is less than that
print 'Total ugly numbers populated ', len(uglies.keys())
print '7th ugly number is ', uglies.keys()[7]
print '10th ugly number is ', uglies.keys()[10]
print '15th ugly number is ', uglies.keys()[15]
print '150th ugly number is ', uglies.keys()[150]