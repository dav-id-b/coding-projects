
#This code takes a string and returns it with each character doubled

p = 'The'

def doubleChar(p):
   
    i  = ''

    for l in p:
       i += l*2
    
    return i

print(doubleChar(p))
