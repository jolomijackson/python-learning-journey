# Username using slicing
first_name = "Julie"
last_name = "Blevins"

def account_generator(first_name, last_name):
  username = first_name[:3] + last_name[:3]
  return username

new_account = account_generator("Julie", "Blevins")
print(new_account)
