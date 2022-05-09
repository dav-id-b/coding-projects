# Given a string, return a string where for every char in the original,
# there are two chars.

# doubleChar('The') → 'TThhee'
# doubleChar('AAbb') → 'AAAAbbbb'
# doubleChar('Hi-There') → 'HHii--TThheerree'

p = 'The'

def doubleChar(p):
   
    i  = ''

    for l in p:
       i += l*2
    
    return i

print(doubleChar(p))
