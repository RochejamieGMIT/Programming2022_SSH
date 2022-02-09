# This program reads in
# a students percentage
# and prints out the
# corresponding grade rounding .5 up 
percentage = float(input("Enter the percentage: "))
#print (percentage)
# be careful with ands and ors
if percentage < 0 or percentage > 100:
 # Later we will show you error handling
 # This should really throw an error
 print ("Please enter a number between 0 and 100")
elif percentage >= 69.5: # we know it is greater than 69.5
 print ("Distinction")
elif percentage >= 59.5: # between 59.5 and 69.4
 print ("Merit2")
elif percentage >= 49.5: # between 49.5 and 59.4
 print ("Merit1")
elif percentage >= 39.5: # between 39.5 and 49.4
 print ("Pass")
else: # the only option left is < 39.5
 print ("Fail")

 
 