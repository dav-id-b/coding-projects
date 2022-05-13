
#This function returns the number of even integers in an array

nums = [2, 1, 2, 3, 4]

def count_evens(nums):
    count = 0
    for digit in nums:
        if digit%2 == 0:
            count+=1
    return count 

print(count_evens(nums))
