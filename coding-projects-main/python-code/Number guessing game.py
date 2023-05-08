#This project runs a random number generator guessing game in the terminal. It gives various hints in regard to guess correctness.


import random

#The following function determines the randomly generated number to be guessed

def rng(): 
    digits = list(range(10))
    random.shuffle(digits)
    digistr = str(digits[0]) + str(digits[1]) + str(digits[2])
    return digistr

guess = input("Please guess a 3 digit number:")

digits = rng()

guess = str(guess)

#The following line of code limits user input to the numbers 0-9

allowchar = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9 }

#The following line of code ensures user input is exactly 3 characters

if len(guess) != 3:
    print("Please ensure your guess is 3 characters long!")    
    
#The following line of code works with line 25 to limit user input to 0-9

elif guess[0] not in allowchar or guess [1] not in allowchar or guess [2] not in allowchar:
    print("Numerical values only, please!")
    
#The following lines of code determine if any, all, or none of the digits input by the user match the rng and will allow the user to continue to guess until successful

while digits != guess:
    
    allowchar = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9 }

    if len(guess) != 3:
        print("Please limit your guess to 3 characters!")

    elif guess[0] not in allowchar or guess [1] not in allowchar or guess [2] not in allowchar:
        print("Numerical values only, please!")

    elif digits[0] == guess[0] or digits[1] == guess[1] or digits[2] == guess[2]:
        print ('Match: You\'ve guessed a correct number in the correct position')
    
    elif guess[0] in digits or guess[1] in digits or guess[2] in digits:
        print('Close: You\'ve guessed a correct number but in the wrong position')

    elif digits[0] == guess[0] or digits[1] == guess[1] or digits[2] == guess[2]:
        print ('Match: You\'ve guessed a correct number in the correct position') 

    else:
        print('Nope: You haven\'t guess any of the numbers correctly')

    guess = input('Please guess again:')

print("Congratulations! You got all three numbers in the correct positions!")
    


    
