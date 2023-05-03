#This function will loop through a list of numbers, updating the largest number as it loops

def max_num(nums):
  maximum = nums[0]
  for number in nums:
    if number > maximum:
      maximum = number
  return maximum


print(max_num([]))
