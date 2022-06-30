weight = float(input("What's your weight(in kg): "))
height = float(input("What's your height(in cm): "))

height = height / 100

BMI =  round(weight/height**2 , 2)

print(f"You're BMI is {BMI}")

if BMI <= 18.5:
    print("You are underweight")
elif 18.5 < BMI <= 24.9:
    print("Your weight is normal")
elif 25 < BMI <= 29.9:
    print("You are overweight")
elif BMI >= 30:
    print("You are obese")