# Your code below: 
first_names = ["Ainsley", "Ben", "Chani", "Depak"]
preferred_size = ["Small", "Large", "Medium"]

preferred_size.append("Medium")
print(preferred_size)

customer_data = [
  ["Ainsley", "Small", True],
  ["Ben", "Large", False],
  ["Chani", "Medium", True],
  ["Depak", "Medium", False]
  ]
print(customer_data)

customer_data[2][2] = False
customer_data[1].remove(False)

customer_data_final = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]
print(customer_data_final)

# Adding the last 2 values in a list together and appending the sum to the original list
def append_sum(my_list):
  for num in range(3):
    my_list.append(sum(my_list[-2:]))
  return my_list

print(append_sum([1, 1, 2]))

# Counting items in a list 
def more_than_n(my_list, item, n):
  if my_list.count(item) > n:
    return True
  else:
    return False

print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

# Sorting concatenated lists
def combine_sort(my_list1, my_list2):
  new_list = my_list1 + my_list2
  new_list.sort()
  return new_list
  sorted_list = sorted(new_list)
  return sorted_list

print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
