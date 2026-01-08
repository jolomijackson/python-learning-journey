print("Enter grades below:")

avg = int()
g1 = int(input("Math: "))
g2 = int(input("Physics: "))
g3 = int(input("English: "))
g4 = int(input("Biology: "))
g5 = int(input("Chemistry: "))

avg += (g1 + g2 + g3 + g4 +  g5) / 5

if avg >= 90:
  print("Grade: A")
elif avg >= 80:
  print("Grade: B")
elif avg >= 70:
  print("Grade: C")
elif avg >= 60: 
  print("Grade: D")
else:
  print("Grade: F")
