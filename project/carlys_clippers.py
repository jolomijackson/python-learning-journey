hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Calculating total price of haircuts last week
total_price = 0
for price in prices:
  total_price += price

# Calculating average price of haircuts last week
average_price = total_price / len(prices)
print("Average Haircut Price:", average_price)

# New prices using list comprehension
new_prices = [price - 5 for price in prices]
print("New Prices:", new_prices)

# Total revenue
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += (prices[i] * last_week[i])
print("Total Revenue:", total_revenue)

# Average daily revenue
average_daily_revenue = total_revenue / 7
print("Average Daily Revenue:", average_daily_revenue)

# Cuts under 30 with list comprehension
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print("Cuts Under $30:", cuts_under_30)
