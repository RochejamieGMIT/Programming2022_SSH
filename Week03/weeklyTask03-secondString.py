# Weekly task 03 - 
# Write a program that asks a user to input a string and outputs every second letter in reverse order.

# Author: Jamie Roche 
inputString = input('enter a string:')

lenghtOfString = len(inputString) - 1
even = lenghtOfString % 2
out = ''

# using the remained of the number of letters left in the stirng divided by 2 to determine if the 
# number is even or odd, allows us to print every second letter. Adding only even numbers to the output
# string 

while lenghtOfString >= 0:
    if even == 0:
     out = out + (inputString[lenghtOfString])
     
    lenghtOfString = lenghtOfString - 1
    even = lenghtOfString % 2
 
print(out)
    




