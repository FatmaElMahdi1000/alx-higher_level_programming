#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
M = number%10 if number > 10 else number % -10
print("last digit of {:d} is {:s} and is".format(number, str(M)), end=" ")

if M > 5: 
    print("greater than 5")
elif M == 0:
    print("0")
else:
    print("less than 6 and not 0")


