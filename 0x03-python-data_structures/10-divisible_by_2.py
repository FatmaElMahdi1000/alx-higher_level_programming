#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    New_list = my_list.copy()
    for i in range(len(New_list)):
        if New_list[i] % 2 == 0:
            return True
        else:
            return False
