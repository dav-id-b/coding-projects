#This is code for a simple "Magic 8-Ball" style interactive game. The user will enter their name & their question, and will be provided with a personalized response & randomly selected answer.

import random

name = input('Please enter your name: ')

question = input('Please ask your question: ')

print(name + ' ' + 'asks' +': ' + question)

answertuple = {'Yes - definitely.', 'It is decidedly so.', 'Without a doubt.', 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'My sources say no.', 'Outlook not so good.', 'Very doubtful.'}

answer = random.choice(tuple(answertuple))

response = 'Magic 8-Ball\'s answer: ' + answer



print(response)