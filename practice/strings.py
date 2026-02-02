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

# Generating username and password
def username_generator(first_name, last_name):
  if len(first_name) > 3:
    first_name = first_name[:3]
  if len(last_name) > 4:
    last_name = last_name[:4]
  user_name = first_name + last_name
  return user_name

def password_generator(user_name):
  password = ""
  for index in range(0, len(user_name)):
    password += user_name[index - 1]
  return password 

username = username_generator("Jolomi", "Jackson")
print(username)
print(password_generator(username))

# Formatting methods
poem_title = "spring storm"
poem_author = "William Carlos Williams"

## Changes string to title form
poem_title_fixed = poem_title.title()
print(poem_title_fixed)

## Changes string to upper case
poem_author_fixed = poem_author.upper()
print(poem_author_fixed)

## Changes string to lower case
poem_author_fixed2 = poem_author.lower()
print(poem_author_fixed2)

# Splitting string
line_one = "The sky has given over"
line_one_words = line_one.split()
print(line_one_words)

## Splitting with index and for loop
authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(",")
print(author_names)

author_last_names = []
for name in author_names:
  name.split()[-1]
  author_last_names.append(name.split()[-1])
print(author_last_names)

## Splitting with escape character
spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""

spring_storm_lines = spring_storm_text.split("\n")
print(spring_storm_lines)
