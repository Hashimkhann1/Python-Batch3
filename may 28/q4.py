m = input("enter message")
o = int(input("enter numeric offset"))
for a in range(len(m)):
    ch = ord(m[a])+o
print(chr(ch))