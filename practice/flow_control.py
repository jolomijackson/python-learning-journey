# Calculator 2.0
print("Welcome to my python Calculator!")

operation = str(input("Enter Operation: "))

num_1 = float(input("First Number: "))
num_2 = float(input("Second Number: "))
if operation == "multiply":
  print(num_1 * num_2)

if operation == "divide":
  print(num_1 / num_2)

if operation == "add":
  print(num_1 + num_2)

if operation == "subtract":
  print(num_1 - num_2)
