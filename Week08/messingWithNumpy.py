# learning numpy

import numpy as np

lsOfNum = [1,2,3,4]
numbers = np.array([1,2,4,5])

#lsOfNum = lsOfNum + 3

numbers = numbers * np.array([1,4,5,6])
print(lsOfNum)
print (numbers)

randomNumbers = np.random.normal(size = 100)

print(randomNumbers)