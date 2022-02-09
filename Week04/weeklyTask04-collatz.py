#Program to At each step calculate the next value by taking the current value and,
# if it is even, divide it by two, but if it is odd, multiply it by three and add one.
#
#
#If less than 1 program does not progress
#using While not 1 to stop program when it reaches 1
#Using elif to decide between odd or even using % 2 = 0 to prove even
#
#
#Author: Jamie Roche

num = int(input("Please enter a positive integer: "))

while num != 1:
    if num < 0:
        num = int(input("Please only enter a positive integer: "))
    elif ((num%2) == 0):
        num = num /2 
        print (str(num))
    else:
        num = (num * 3) + 1
        print (str(num))
    
