#!/usr/bin/python3
def multiple_returns(sentence):

    lenght = len(sentence)
    if len(sentence) > 0:
        tuple = (len(lenght), sentence[0])
        return tuple
    else:
        None
