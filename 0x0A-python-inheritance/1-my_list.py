#!/usr/bin/python3
"""
A class for sorting number
"""


class MyLis(list):
    def __init__(self, number):
        super().__init(number)

    def print_sorted(self):
        print(f"Sorted list: {sorted(self)}")
