#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

        Row = []
        Col = []
        for i, value in enumerate(Row):
            new_row = []
            for m in range(len(Col)):
                New_value = (value * Col[m]) ** 2  #I only added this **2 to get the square
                new_row.append(New_value)
            matrix.append(new_row)
            for row in matrix:
                print(row)
