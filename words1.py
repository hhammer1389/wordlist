import numpy as np
def num_letters(n_rows, n_columns):
    return n_rows * n_columns - (n_rows-2) * (n_columns-2)
assert num_letters(4,4)== 12
assert num_letters(4,13)== 30
assert num_letters(6,4)==16
assert num_letters(6,7)==22
print("Checking assertions")

