#Program to count how many e or E's in a text file that is read in from command line. 
# assuming by counting up e's user intends both lower and capital e's
# 
# 
# Author: Jamie Roche
#Reference to read in from command line:
#https://stackoverflow.com/questions/7439145/i-want-to-read-in-a-file-from-the-command-line-in-python

import sys
with open(sys.argv[1], 'r') as f: # reading in document from cmd line
    cmdText = f.read()
#print (cmdText) - line to test if reading in was working 

count = 0 # Initalise count of e to 0
for key in cmdText: #Parse through each character to check if it is an e or an E. Adding to the counter if it is.
    if (key == "e" or key == "E"):
        count += 1
    
print(count) # printing out the count for the user
