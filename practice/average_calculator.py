# Average Calculator
print("Final Year Grades!")
english = 89
math = 86
physics = 90
chemistry = 81
psychology = 85
average = int()

print("English: ", english, "\nMath: ", math, "\nPhysics: ", physics, "\nChemistry: ", chemistry, "\nPsychology: ", psychology)

average += (english + math + physics + chemistry + psychology) / 5
print("Average: ", average)

cutoff = 85

if average < cutoff:
  print("You didn't make the cut :(")
else:
  print("You made the cut!")
