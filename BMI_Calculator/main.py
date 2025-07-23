weight = float(input("Enter the weight in kgs: "))
height = float(input("Enter the height in metres: "))
if weight > 0 and height >0:
    bmi = (weight/(height) **2)
    if bmi < 18.5:
        print("You are in underweight ", bmi)
    elif bmi >= 18.5 and bmi <=24.9:
        print("You are in normal healthy weight",bmi)
    elif bmi >=25 and bmi <=29.9:
        print("You are Overweighted",bmi)
    elif bmi >=30:
        print("Obesity",bmi)
else:
    print("Enter only +ve values")
