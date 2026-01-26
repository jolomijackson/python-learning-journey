# Adding greetings to names in a list
def add_greetings(names):
  greeting = []
  for name in names:
    greeting.append("Hello, " + name)
  return greeting

print(add_greetings(["Owen", "Max", "Sophie"]))

# Checking if a number is in range
def in_range(num, lower, upper):
  if num >= lower and num <= upper:
    return True
  else:
    return False
    
print(in_range(10, 10, 10))
# should print True
print(in_range(5, 10, 20))
# should print False

# Checking the same name 
def same_name(your_name, my_name):
  if your_name == my_name:
    return True
  else:
    return False

print(same_name("Colby", "Colby"))
# should print True
print(same_name("Tina", "Amber"))
# should print False

# Movie review
def movie_review(rating):
  if rating <= 5:
    return "Avoid at all costs!"
  elif rating < 9:
    return "This one was fun."
  else:
    return "Outstanding!"

print(movie_review(9))
# should print "Outstanding!"
print(movie_review(4))
# should print "Avoid at all costs!"
print(movie_review(6))
# should print "This one was fun."
