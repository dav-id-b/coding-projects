#Given an array of ints, return the number of 9's in the array.

def array_count9(nums):
  
  count = 0
  
  for desired in nums:
    if desired == 9:
      count = count + 1
      
  return count
