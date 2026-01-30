# Username using slicing
first_name = "Julie"
last_name = "Blevins"

def account_generator(first_name, last_name):
  username = first_name[:3] + last_name[:3]
  return username

new_account = account_generator("Julie", "Blevins")
print(new_account)

first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name, last_name):
  temp_password = first_name[len(first_name)-3:] + last_name[len(last_name)-3:]
  return temp_password

temp_password = password_generator("Reiko", "Matsuki")
print(temp_password)


# Editing string using slicing and concatenation
first_name = "Bob"
last_name = "Daily"

fixed_first_name = "R" + first_name[1:]
print(fixed_first_name)


# Using backslash to include " in the string
password = "theycallme\"crazy\"91"


# Checking for a letter in a word
def letter_check(word, letter):
  for alph in word:
    if alph == letter:
      return True
  return False

print(letter_check("strawberry", "a"))
print(letter_check("strawberry", "o"))

def contains(big_string, little_string):
  return little_string in big_string

print(contains("oritsejolomi", "jackson"))

def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    if letter in string_two and not letter in common:
      common.append(letter)
  return common

print(common_letters("oritsejolomi", "jackson"))


# Counting a string without len function
def get_length(string):
  counter = 0
  for num in string:
    counter += 1
  print(counter)

get_length("test")
