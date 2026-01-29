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
