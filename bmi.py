def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight= " + str(weight))
    bmi = weight/(height*height)
    print("BMI= " + str(round(bmi, 2)))
    if bmi < 18.5:
        print("Underweight")
        weightclass = -1
    elif 18.5 <= bmi <= 25:
        print("Normal weight")
        weightclass = 0
    elif bmi > 25:
        print("Overweight")
        weightclass = 1


calculate_bmi(weight=57, height=1.73)