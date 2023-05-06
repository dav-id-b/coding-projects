#this code serves as a tool to keep track of the progress of a scrabble game


#the following two lines are the basis for the letter scoring system
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#this serves to create a dictonary of the letters and their corresponding values
letter_to_points = {key:value for key, value in zip(letters, points)}

#this has been added to take into account "blank tiles" with a score value of 0
letter_to_points[' '] = 0

#this scores the words played (taking case into account) and adds them to a running total of points
def score_word(word):
  word = word.upper()  
  point_total = 0
  for letter in word:    
    letter = letter_to_points.get(letter)
    point_total += letter    
  return point_total

#this dictionary corresponds each player to their respective words
player_to_words = {'player1': [ ], 'player2': [ ], 'player3': [ ], 'player4': [ ] }

#this dictionary will be filled with players points by the code following it
player_to_points = {}

#this goes through the dictonary containing the players & their word lists to calculate their score
for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points

#this updates the word list and point total for an individual player
def play_word(player, word):
  player_to_words[player] += [word] 
  player_to_points[player] += score_word(word)

#this updates the word list and point total for all players
def update_point_totals(player, word, player_to_points):
    play_word(player, word)
    player_to_points[player] += score_word(word)
    print(player_to_points)
