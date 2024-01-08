#!/usr/bin/python3

def print_last_digit(number):

    number = str(number)
    length = len(number)
    last_digit = int(number[length-1])
    print("Last digit:", last_digit)
