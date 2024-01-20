def complex_delete(a_dictionary, value):
    while value in a_dictionary.values():
        for M, v in a_dictionary.items():
            if v == value:
                del a_dictionary[M]
                break

    return (a_dictionary)
