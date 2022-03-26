# Learning about except

from tkinter import N


#filename = 'data.txt'
import sys

filename = sys.argv[1]


#print(sys.argv)

try:

    with open(filename) as f:
        print (f.read())
        var =10/0
except FileNotFoundError:
    print("File name does not exist")
except:
    print("error")

