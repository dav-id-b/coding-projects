#These two functions will take the user's first & last names as input, and will turn them into a username & temporary password
#If the user's first name is less than 3 characters, or their last name is less than 4 characters, the respective name will be included in full
#The temporary password will be generated as the username with the last character shifted to the front

def username_generator(first_name, last_name):
  username = ''
  if len(first_name) < 3 and len(last_name) < 4:
    username = first_name + last_name
  elif len(first_name) < 3:
    username = first_name + last_name[:4]
  elif len(last_name) < 4:
    username = first_name[:3] + last_name
  else:
    username = first_name[:3] + last_name[:4]    
  return username


def password_generator(username):
  password = ''
  for i in range(0, len(username)):
    password += username[i - 1]
  return password
