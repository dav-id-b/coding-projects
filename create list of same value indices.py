#This function will compare two lists of numbers and return a list composed of indices where the numbers match

def same_values(lst1, lst2):
  samelst = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
        samelst.append(index)
  return samelst


print(same_values())
