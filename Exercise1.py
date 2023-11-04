def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight= " + str(weight))
    bmi = weight/(height*height)
    print("BMI= " + str(round(bmi, 2)))
    if bmi < 18.5:
        print("Underweight")
    elif 18.5 <= bmi <= 25:
        print("Normal weight")
    elif bmi > 25:
        print("Overweight")


calculate_bmi(weight=57, height=1.73)