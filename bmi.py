def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight= " + str(weight))
    val_bmi = weight/(height*height)
    print("BMI= " + str(round(val_bmi, 2)))
    if val_bmi < 18.5:
        weightclass = -1
        print("Underweight, weight class is", weightclass)
    elif 18.5 <= val_bmi <= 25:
        weightclass = 0
        print("Normal weight, weight class is", weightclass)
    elif val_bmi > 25:
        weightclass = 1
        print("Overweight, weight class is", weightclass)


calculate_bmi(weight=57, height=1.73)