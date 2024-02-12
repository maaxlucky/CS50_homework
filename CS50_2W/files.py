import os

# same function as "ls" but in python
print(os.popen('ls').read())