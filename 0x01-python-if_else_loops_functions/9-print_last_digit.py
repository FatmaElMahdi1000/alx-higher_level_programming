#!/usr/bin/python3

def print_last_digit(number):

    number = str(number)
    length = len(number)
    last_digit = int(number[-1])
    print(last_digit, end="")
    return last_digit
