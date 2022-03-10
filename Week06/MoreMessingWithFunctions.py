


def readNum(message = "enter a number "):
    num = False
    while(num == False):
        try:
         num = int(input(message))
        except ValueError:
          print("just numbers no letters ",end ='')
    return num

num1 = readNum()
num2 = readNum("enter num2 please ")

answer = num1 * num2
print (answer)