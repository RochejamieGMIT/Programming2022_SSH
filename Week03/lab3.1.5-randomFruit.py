# This program prints out a random fruit
# Updated program to user random.choice instead of 
# index = random.randint(0,len(fruits)-1)

import random
fruits = ('Apple', 'Orange', 'Banana', 'Pear')

fruit = random.choice(fruits)
print("A Random Fruit:{}".format(fruit))
