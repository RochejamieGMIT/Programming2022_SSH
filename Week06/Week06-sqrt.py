#Find the square root using functions, newton method
#
#Author: Jamie Roche
#References: https://www.youtube.com/watch?v=2158QbsunA8
# https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo
# https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/#:~:text=Let%20N%20be%20any%20number,correct%20square%20root%20of%20N.
def sqrt(ToRoot, RError) :
    #Pass in the number to root and the allowable error
    #Set the first check to be the number itself
    x = ToRoot
 
    
    Check = False # Set up while loop until correct margin of error is reached
    while (not Check) :
        root = 0.5 * (x + (ToRoot / x))
 
        # Check to see if the differce is within the allowable margin
        if (abs(root - x) < RError) :
            Check = True
 
        x = root
 
    return root # Return the square root of the number

#Reusing the code for the correct input type to allow different numbers to be squared
def readNum(message = "enter a number "):
    num = False
    while(num == False):
        try:
         num = int(input(message))
        except ValueError:
          print("just numbers no letters ",end ='')
    return num

#Reusing the code for the correct input type to allow the user select the accuarcy of the square root
#The smaller the floating point entered, the more accurate the result.
def readFloat(message = "enter a how acurate you want the estimate to be. The smaller the floating point, the more accurate the estimation will be Enter a float. "):
    num = False
    while(num == False):
        try:
         num = float(input(message))
        except ValueError:
          print("Pleaes enter a floating point numbrt",end ='')
    return num

    

NumToRoot = readNum()
Accuracy  = readFloat()

Sqroot = (sqrt(NumToRoot, Accuracy)) # Choosing to set the returned value to a variale before printing out incase other calculations could be required

print(Sqroot)