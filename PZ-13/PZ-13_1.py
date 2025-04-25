"""
Перенести в новый двумерный список Matr1 элементы, которые не находятся в
первых и последних строках и столбцах матрицы Matr2 произвольного размера
"""

import random
size_matrix = range(random.randint(4, 6))

matrix_2 = [[j*random.randint(10, 100) for j in size_matrix] for i in range(random.randint(4, 6))]
matrix_1 = [[j for j in i if j != matrix_2[matrix_2.index(i)][0] and j != matrix_2[matrix_2.index(i)][-1]] for i in matrix_2 if  i != matrix_2[0] and i != matrix_2[-1]]



print("\033[0;32m------------------------------Matrix_2--------------------------------\x1b[0;37m")
for i in matrix_2:
    print(i)

print("\n\033[0;32m------------------------------Matrix_1--------------------------------\x1b[0;37m")

for i in matrix_1:
    print(i)

