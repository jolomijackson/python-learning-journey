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

# Exponents with 2 lists
def exponents(bases, powers):
  answers = []
  for base in bases:
    for power in powers:
      answers.append(base ** power)
  return answers

print(exponents([2, 3, 4], [1, 2, 3]))

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

# Finding the list with a larger sum
def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  for num in lst1:
    sum1 += num
  for num in lst2:
    sum2 += num
  if sum1 >= sum2:
    return lst1
  else:
    return lst2
  
print(larger_sum([1, 9, 5], [2, 3, 7]))

# Number over 9000
def over_nine_thousand(lst):
  lst_sum = 0
  for num in lst:
    lst_sum += num
    if lst_sum > 9000:
      break
  return lst_sum
  
print(over_nine_thousand([8000, 900, 120, 5000]))

# Maximum number
def max_num(nums):
  max = nums[0]
  for num in nums:
    if num > max:
      max = num
  return max

print(max_num([50, -10, 0, 75, 20]))

# Matching indices
def same_values(lst1, lst2):
  matching_index = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      matching_index.append(index)
  return matching_index

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

# Reversed list
def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True

print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))
