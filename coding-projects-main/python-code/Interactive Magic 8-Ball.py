#This is code for a simple "Magic 8-Ball" style interactive game. The user will enter their name & their question, and will be provided with a personalized response & randomly selected answer.

import random

#This line prompts the user to enter their name using the input function
name = input('Please enter your name: ')

#This line prompts the user to enter a question, also using the input function
question = input('Please ask your question: ')

#This will print out a combination of the user's name and their question in a readable format
print(name + ' ' + 'asks' +': ' + question)

#This line contains all of the possible answers to the user's question. Need to add functionality for "try again prompt" 
answertuple = {'Yes - definitely.', 'It is decidedly so.', 'Without a doubt.', 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'My sources say no.', 'Outlook not so good.', 'Very doubtful.'}

#This will randomly select an answer from the previous line of code
answer = random.choice(tuple(answertuple))

#This will forumlate the response using the randomly selected answer
response = 'Magic 8-Ball\'s answer: ' + answer

#Finally, this prints out the answer to the user's question in a readable form 
print(response)
