# Your code below:
# Pizza toppings
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

# Pizza prices
prices = [2, 6, 1, 3, 2, 7, 2]

# Number of 2 dollar slices
num_two_dollar_slices = prices.count(2)

# Number of pizza toppings
num_pizzas = len(toppings)

print("We sell", num_pizzas, "different kinds of pizza!")

# Toppings and their prices
pizza_and_prices = [
  [2, "pepperoni"],
  [6, "pineapple"],
  [1, "cheese"],
  [3, "sausage"],
  [2, "olives"],
  [7, "anchovies"],
  [2, "mushrooms"]
]

# Pizzas from cheapest to priciest
pizza_and_prices.sort()
print(pizza_and_prices)
print("\n")

# Cheapest Pizza
cheapest_pizza = pizza_and_prices[0]
print("The cheapest pizza is: ", cheapest_pizza)
print("\n")

# Priciest Pizza
priciest_pizza = pizza_and_prices[-1]
print("The priciest pizza is: ", priciest_pizza)
print("\n")

# Removing a slice
pizza_and_prices.pop(-1)
print("A customer bought: ", priciest_pizza)
print("\n")

# Adding new slice
pizza_and_prices.insert(4, [2.5, "peppers"])
print("Updated pizza list: ", "\n", pizza_and_prices)
print("\n")

three_cheapest = pizza_and_prices[:3]
print("Three of the cheapest slices are: ", "\n", three_cheapest)
