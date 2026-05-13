print("Is it a leap year?")
year = int(input("Enter a year: "))

if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
    result = "is a leap year."
else:
    result = "is not a leap year."

print("The year " + str(year) + " " + result)
