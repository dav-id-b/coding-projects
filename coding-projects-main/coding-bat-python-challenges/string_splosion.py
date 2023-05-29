#Given a non-empty string like "Code" return a string like "CCoCodCode".

def string_splosion(str):
  finalstr = ''
  
  for char in range(len(str)):
    finalstr = finalstr + str[:char+1]
    
  return finalstr
