#В двумерном списке отрицательные числа возвести в квадрат

import random
size_matrix = range(random.randint(10, 20))
matrix = [[j*random.randint(-10, 10) for j in size_matrix] for i in range(random.randint(5, 20))]
matrix_new = [[j**2 if j < 0 else j for j in i] for i in matrix]


print("\033[0;32m------------------------------Matrix--------------------------------\x1b[0;37m")
for i in matrix:
    print(i)

print("\n\033[0;32m------------------------------Matrix_new--------------------------------\x1b[0;37m")
for i in matrix_new:
    print(i)