single_digits = range(10)
squares = []

for digit in single_digits:
  print(digit)
  squares.append(digit ** 2)

print(squares)

cubes = [digit ** 3 for digit in single_digits]
print(cubes)

# Numbers divisible by 10
def divisible_by_ten(nums):
  count = 0
  for num in nums:
    if num % 10 == 0:
      count += 1
  return count

print(divisible_by_ten([20, 25, 30, 35, 40]))

# Adding greetings to names in a list
def add_greetings(names):
  greeting = []
  for name in names:
    greeting.append("Hello, " + name)
  return greeting

print(add_greetings(["Owen", "Max", "Sophie"]))

# Removing the first value if it's even
def delete_starting_evens(my_list):
  while len(my_list) > 0 and my_list[0] % 2 == 0:
    my_list = my_list[1:]
  return my_list

print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

# Selecting values with odd index from a list
#Write your function here
def odd_indices(my_list):
  odd_index = []
  for index in range(len(my_list)):
    if index % 2 == 1:
      odd_index.append(my_list[index])
  return odd_index

OR

def odd_indices(my_list):
  odd_index = []
  for index in range(1, len(my_list), 2):
    odd_index.append(my_list[index])
  return odd_index
  
print(odd_indices([4, 3, 7, 10, 11, -2]))
