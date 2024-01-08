#!/usr/bin/python3

def islower(c):

    c = ord(c)
    if c >= 97 and c <= 122:
        print("{}".format(chr(c)))
        c = c + 1
        return True
    else:
        return False
