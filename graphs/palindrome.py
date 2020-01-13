s = "abaab"
# 8

def is_substr_palindrome(left, right):
    if left < 0 or right >= n:
        return False
    if left == right:
        return True
    print left, right, s[left], s[right]
    return s[left] == s[right]

n = len(s)
palindrome_count = 0
for chunk_size in range(0, 2):
    for index in range(n):
        substr = s[index:index + chunk_size]
        print (substr)
        left_index = index
        right_index = index + chunk_size 
        is_palindrom = is_substr_palindrome(left_index, right_index)
        while is_palindrom:
            palindrome_count += 1
            # expand on left and right and check if it is palindrom
            # if left_index == 0 or right_index == n:
            #     break
            left_index = left_index - 1
            right_index = right_index + 1
            is_palindrom = is_substr_palindrome(left_index, right_index)
            
print ('result ', palindrome_count)

# print "Hello World"
