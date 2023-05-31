#Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

def array123(nums):
  desired = "123"
  strlist = map(str, nums)
  numstr = ''.join(strlist)
  if desired in numstr:
    return True
  else:
    return False
