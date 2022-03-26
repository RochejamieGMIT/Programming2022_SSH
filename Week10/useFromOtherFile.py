# using a module from another file 

from personModule import *

person1 = {
        'firstname' : 'Jamie',
        'lastname' : 'Roche',
        'dob' : dt.date(1995,1,20),
        'height' : 183,
        'weight' : 93

    }

displayperson(person1)
getHealthData(person1)