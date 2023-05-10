#This is an expanded version of my first phrasal template game project, using the format method as opposed to string concatenation

#This wall of code allows for user input for the missing words - there is likely some way to streamline this
adj1 = input('Please enter an adjective:')
adj2 = input('Please enter another adjective:')
bird = input('Please enter a type of bird:')
room = input('Please enter the name of a room in a house:')
verbpst = input('Please enter a past tense verb:')
verb = input('Please enter a verb:')
relname = input('Please enter a relative\'s name:')
noun = input('Please enter a noun:')
liq = input('Please enter a liquid:')
verbing1 = input('Please enter a verb ending in -ing:')
parts = input('Please enter a body part (plural):')
plurnoun = input('Please enter a plural noun:')
verbing2 = input('Please enter another verb ending in -ing:')
noun2 = input('Please enter another noun:')

#The following code indicates where the user inputted words will be inserted

lib = 'It was a {0}, cold November day. I woke up to the {1} smell of {2} roasting in the {3} downstairs. I {4} down the stairs to see if I could help {5} the dinner. My mom said, "See if {6} needs a fresh {7}." So I carried a tray of glasses full of {8} into the {9} room. When I got there, I couldn\'t believe my {10}! There were {11} {12} on the {13}!'

#This code uses the string formatting method to insert the user inputted words into the template, and prints the final result

print(lib.format(adj1, adj2, bird, room, verbpst, verb, relname, noun, liq, verbing1, parts, plurnoun, verbing2, noun2))