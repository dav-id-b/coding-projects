#This function will count & return the number of 7's present in an array
#Swapping out the 7 for another number will cause it to check for the prescence of that number instead

def array_count(nums):
  
  count = 0
  
  for desired in nums:
    if desired == 7:
      count += 1
      
  return count
