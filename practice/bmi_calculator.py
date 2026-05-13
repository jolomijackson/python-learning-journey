print("Welcome to the BMI calculator!!")
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))
b_m_i = (weight / (height) ** 2) * 10000

if b_m_i < 18.5:
    remark = "You're underweight!"
elif b_m_i <= 24.9:
    remark = "You're at a healthy weight!"
elif b_m_i <= 29.9:
    remark = "You're overweight!"
elif b_m_i >= 30.0:
    remark = "You're obese!"

print("Your BMI is " + str(round(b_m_i, 2)) + ". " + remark)
