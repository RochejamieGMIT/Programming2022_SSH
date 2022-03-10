# messing with os

import os

filename = 'test.txt'
if os.path.exists(filename):
    print(filename, "already exists")
    os.remove(filename)
    
else:
    print(filename, "does not exist, Want to creat it?")
    