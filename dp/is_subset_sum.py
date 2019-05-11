def is_subset_sum(arr, n, sum):
    subset = [[False for i in range(sum+1)] for i in range(n+1)]

    # if sum is 0, then answer is true
    for i in range(n+1):
        subset[i][0] = True

        # if sum is not 0, set is empty, then answer is False
        for i in range(1, sum+1):
            subset[0][i] = False

        # fill the subset table in bottom up manner
        for i in range(1, n+1):
            for current_sum in range(1, sum+1):
                current_element = arr[i - 1]
                if current_sum < current_element:
                    subset[i][current_sum] = subset[i - 1][current_sum]
                if current_sum >= current_element:
                    subset[i][current_sum] = (subset[i - 1][current_sum]
                                    or subset[i-1][current_sum - current_element])
    return subset




# A recursive solution for subset sum 
# problem 

# Returns true if there is a subset 
# of set[] with sun equal to given sum 
def isSubsetSum(arr,n, sum, result):
    if result[n][sum] is not None:
        return result[n][sum]
    print 'calling is subset for n : ', n, ' and sum : ', sum
    # Base Cases 
    if (sum == 0) : 
        result[n][sum] = True
        return result[n][sum]
    if (n == 0 and sum != 0) : 
        result[n][sum] = False
        return result[n][sum]

    # If last element is greater than 
    # sum, then ignore it 
    if (arr[n - 1] > sum) : 
        result[n][sum] = isSubsetSum(arr, n - 1, sum, result)
        return result[n][sum]

    # else, check if sum can be obtained 
    # by any of the following 
    # (a) including the last element 
    # (b) excluding the last element 
    value = isSubsetSum(arr, n-1, sum, result) or isSubsetSum(arr, n-1, sum-arr[n-1], result) 
    result[n][sum] = value
    return value
    
    
# Driver program to test above function 
set = [3, 34, 4, 12, 5, 2] 
sum = 9
n = len(set) 
result = [[None for i in range(sum+1)] for i in range(n+1)]
isSubsetSum(set, n, sum, result)
print result

arr = [3, 34, 4, 12, 5, 2]
sum = 9
n = 6
answer2 = is_subset_sum(arr, n, sum)


print answer2
print ('\n\n\n****\n\n\n')
for i in range(len(result)):
    for j in range(len(result[i])):
        if result[i][j] is not None:
            print result[i][j] == answer2[i][j]
