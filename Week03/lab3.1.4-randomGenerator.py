# program that prints out a random number between two numbers set by user
import random

x = int(input("Enter the first parameter for the random number: "))
y = int(input("Enter the second parameter for the random number: "))

number = random.randint(x,y)
print("here is a random number {}".format(number))