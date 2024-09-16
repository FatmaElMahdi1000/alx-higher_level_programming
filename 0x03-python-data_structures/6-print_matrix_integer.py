
#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i, value1 in enumerate(Row):
        new_row = []
        for x, value2 in enumerate(Col):
            New_value = value1 * value2
            new_row.append(New_value)
        matrix.append(new_row)
    for row in matrix:
        print(row)
