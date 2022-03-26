# learnig aabout objects

class Nameofclass:
    name = ""
    last = ''
    def getfullname(self):
        return self.name + ' ' + self.last
    pass

inst = Nameofclass()
inst2 = Nameofclass()

inst.name = 'Jamie'
inst2.last = 'Roche'
person = inst
print (person.name)

inst.last = 'bloggs'
print (person.getfullname())

str1 = "baaaaaaaa"
str2 = str1

str1 += " werwtew"

print(str2)