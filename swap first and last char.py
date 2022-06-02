#This function returns a string with the first & last index of it swapped 


def front_back(str):

  if len(str) > 1:
    newstr = str[-1] + str[1:-1] + str[0]
    return newstr
  
  
  else:
    return str