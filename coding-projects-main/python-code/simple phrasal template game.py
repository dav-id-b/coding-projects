#The following code is for a very simple, but easily modified "mad libs"-style game 

#The user will be prompted to enter several different words of different types, and the code will assemble them into a "fun" sentence

adjective1 = input('Please enter an adjective:')

verb1 = input('Please enter a verb:')

adjective2 = input('Please enter another adjective:')

lib = 'The ' + adjective1 + ' dog would like to ' + verb1 + ' the tree, but it is too ' + adjective2 + '.'

print(lib)
