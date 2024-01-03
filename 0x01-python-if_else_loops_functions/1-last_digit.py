#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
M = number%10
print(f"last digit of {number} is " + str(M) + " and is", end=" ")

if M > 5: 
    print("greater than 5")
elif M == 0:
    print("0")
else:
    print("less than 6 and not 0")


