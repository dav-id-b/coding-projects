#This function returns the difference between n & 21.
#If n is greater than 21, it will return the difference doubled.

def diff21(n):
  if n < 21:
    return 21 - n
  else:
    return (n-21)*2
