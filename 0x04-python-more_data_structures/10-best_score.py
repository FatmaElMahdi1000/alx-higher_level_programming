#!/usr/bin/python3

def best_score(a_dictionary):
    largest_k = max(a_dictionary, key=a_dictionary.get)
    return largest_k
