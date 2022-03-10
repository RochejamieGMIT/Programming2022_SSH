# Messing with files

filename = 'test.txt'
with open(filename, 'r+') as f:
    f.write("Hello World")

    f.seek(0)
    data = f.readline()
    print (data)

    print ("done")

    filename = 'testread.txt'

  #  with open(filename, "r") as f:
    #   data = f.read()
    #    print(data)


with open("messingWithFiles.py", "rt") as f:
    for line in f:
        print ("line", line[:-1]) # [;-1] removes return 
 

