weight = 63

# Ground Shipping
if weight <= 2:
  cost = (weight * 1.50) + 20.00
elif weight > 2 and weight <= 6:
  cost = (weight * 3.00) + 20.00
elif weight > 6 and weight <= 10:
  cost = (weight * 4.00) + 20.00
else:
  cost = (weight * 4.75) + 20.00

print("Ground shipping cost: $", cost)

cost_premium = 125.00
print("Ground shipping premium cost: $", cost_premium)

# Drone Shipping
if weight <= 2:
  cost_drone = (weight * 4.50) 
elif weight > 2 and weight <= 6:
  cost_drone = (weight * 9.00) 
elif weight > 6 and weight <= 10:
  cost_drone = (weight * 12.00) 
else:
  cost_drone = (weight * 14.25) 

print("Drone shipping cost: $", cost_drone)

# Cheapest Method
if (cost < cost_premium) and (cost < cost_drone):
  print("Ground shipping is the cheapest.")
elif (cost_premium < cost) and (cost_premium < cost_drone):
  print("Ground shipping premium is the cheapest")
elif (cost_drone < cost) and (cost_drone < cost_premium):
  print("Drone shipping is the cheapest")
