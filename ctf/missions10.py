# --------------------- Question: ---------------------
# http://ctfs.me/missions/10

print("You Entered private room!")
user_input = raw_input("Enter Password: ")

if len(user_input) != 10:
    print "Try Again!"
    exit()
flag = [233, 129, 9, 5, 130, 194, 195, 39, 75, 229]
user_str = []
for char in user_input:
    print char
    user_str.append( (((ord(char) << 5) | (ord(char) >> 3)) ^ 111) & 255 )

if (user_str == flag):
    print "Well Done"
else:
    print "Try Again!"


#--------------------- Answered: ---------------------
import string
chrs = string.printable.replace(' \t\n\r\x0b\x0c', '')
joins = ' '.join(chrs).split()
out = []
for char in chrs:
    out.append( (((ord(char) << 5) | (ord(char) >> 3)) ^ 111) & 255 )

flag = [233, 129, 9, 5, 130, 194, 195, 39, 75, 229]
jutul = ''
for item in flag:
    if item in out:
        fuck = out.index(item)
        jutul += joins[fuck]
    else:
        pass

print jutul

>>> 4w3SomeB!T
