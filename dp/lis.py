arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
# arr = [50, 3, 10, 7, 40, 80]
lis = []
# 10 22 33 50 60 80
# 22 33 50 60 80
# 9 33 50 60 80
# 9 21 41 60 80
# 33 41 60 80
# 33 50 60 80
# 50 60 80
# 41 60 80
# 60 80
# 80 


#     10    22    9     33    21    50    41    60    80

# 10  F     T     F     T     T    T      T     T     T
# 22  F     F     F     T     F    T      T     T     T
# 9   T     F     F     T     T    T      T     T     T
# 33  F     F     F     F     F    T      T     T     T
# 21  F     T     F     T     F    T      T     T     T
# 50  F     F     F     F     F    F      F     T     T
# 41  F     F     F     F     F    T      F     T     T
# 60  F     F     F     F     F    F      F     F     T
# 80  F     F     F     F     F    F      F     F     F



def lis(arr):
    n = len(arr)
    lis = [0 for i in range(n)]
    for i in range(1, n):
        if arr[i] > arr[i-1]:
            lis[i] = lis[i-1] + 1
        else:
            lis[i] = lis[i-1]

    print lis

arr = [10, 22, 9, 33, 21, 50, 41, 60] 
print "Length of lis is", lis(arr) 
