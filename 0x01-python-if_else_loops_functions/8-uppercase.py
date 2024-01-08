#!/usr/bin/python3

def islower(c):
    c = ord(c)
    if c >= 97 and c <= 122:
        return True
    else:
        return False

def uppercase(str):

    for c in str:
        print({:c}.format(ord(c)) if not islower(c) else ord(c) - 32,
                end="")
        print("")
