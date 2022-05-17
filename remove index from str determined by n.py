#This code removes a character from a specific index in a string, determined by n

def missing_char(str, n):
  
  strlist = list(str)
  
  del strlist[n]
  
  str = ''.join(strlist)
  
  return str
 
  