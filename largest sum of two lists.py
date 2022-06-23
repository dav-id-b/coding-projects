#This function will loop through two lists, determining which has a greater sum

def larger_sum(lst1, lst2):
  sum1 = sum(lst1)
  sum2 = sum(lst2)
  if sum2 > sum1:
    return lst2
  else:
    return lst1


print(larger_sum([], []))
