# bmi.py
# Programme to calculate bmi
# Author: Jamie Roche 



weight = int(input("Enter your weight(kg)"))
height = int(input("Enter your height(cm)"))

bmi = (weight/(height**2))*10000

print("Your BMI is {:.1f}" .format(bmi))