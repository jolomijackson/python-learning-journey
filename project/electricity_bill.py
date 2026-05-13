print("Advanced Electricity Bill Calculator")
units = float(input("Enter the number of units: "))
remainder = units
tier_list = [(50, 0.50), (100, 0.75), (100, 1.20), (remainder, 1.50)]
bill = 0
remainder = units

for tier in tier_list:
    charged_units = min(tier[0], remainder)
    amount_per_unit = tier[1]
    bill += charged_units * amount_per_unit
    remainder -= charged_units
    
surcharge = bill * 0.20
final_bill = bill + surcharge
print("Your Electricity bill for " + str(units) + " units is $" + str(final_bill) + ".")
