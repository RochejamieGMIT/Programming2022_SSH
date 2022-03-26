# Learning about modules
import datetime as dt
def getHealthData(person):
    print("get health data: ", person['firstname'])

def displayperson(person):
    print(person)

if __name__== '__main__':

    person1 = {
        'firstname' : 'Jamie',
        'lastname' : 'Roche',
        'dob' : dt.date(1995,1,20),
        'height' : 183,
        'weight' : 93

    }

    displayperson(person1)
    getHealthData(person1)

    