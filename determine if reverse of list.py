#This function will loop through two lists to determine if one has the numbers in reverse order of the other

def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True


print(reversed_list([], []))
print(reversed_list([], []))
