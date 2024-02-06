#!/usr/bin/python3

"""This is printing name, Method"""


def say_my_name(first_name, last_name=""):
    """
    Args:
        string1
        string2
    Output:
          'My name is <first name> <last name>'
    Raise:
         TypeError
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name}{last_name}")

    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/3-say_my_name.txt")
