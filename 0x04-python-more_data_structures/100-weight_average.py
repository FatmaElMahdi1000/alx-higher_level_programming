#!/usr/bin/python3

def weight_average(my_list=[]):
    New_list1 = []
    New_list2 = []
    if my_list == []:
        return {}.format()
    for i, value in enumerate(my_list):
        value1 = value[0]
        value2 = value[1]
        result1 = value1 * value2
        result2 = value2
        New_list1.append(result1)
        New_list2.append(result2)
    updated_list1 = sum(New_list1)
    updated_list2 = sum(New_list2)
    return updated_list1/updated_list2
