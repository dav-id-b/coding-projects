

#This code returns the sum of three integers (a, b, c,). However, if any of the values is in the range of 13-19, the value counts as 0. 15 & 16 are excluded from this, and retain their values.

a = 19
b = 15
c = 12

def no_teen_sum(a, b, c):
    
    if a in range(13,20):
        a = fix_teen(a)

    if b in range(13,20):
        b = fix_teen(b)   

    if c in range(13,20):
        c = fix_teen(c)   
    i = sum([a,b,c]) 
    return i 
     


def fix_teen(n):
    if n in range(15,17):
        return n 
    else:
        return 0




print(no_teen_sum(a,b,c))
