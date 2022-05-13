#This code determines if either one of two strings is found at the very end of the other, ignoring letter case. 

a = 'Hiabc'

b = 'abc'

def end_other(a, b):
  a.lower()
  b.lower()
  
  if len(a) >= len(b):
    if a[len(a)-len(b):] == b:
      return True 
  else:
    if b[len(b)-len(a):] == a:
      return True
    
  return False

print(end_other(a,b))

