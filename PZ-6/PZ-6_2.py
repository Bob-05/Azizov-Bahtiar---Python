# Дан список размера N.
# Найти номера тех элементов списка, которые больше своего правого соседа, и количество таких элементов.
# Найденные номера выводить в порядке их возрастания.

import random

def check(type_string):
    value = input(type_string)

    while type(value) != int:
        try:
            value = int(value)
            if type(value) == int:
                return value
        except ValueError:
            print("TypeError!!!")
            value = input(type_string)



a = list()
limit_n = check('Enter limits for list a: ')
largest_numbers = list()

for i in range(limit_n):
    a.append(random.randint(1, 100))


for i in range(limit_n - 1):
    if a[i] > a[i + 1]:
        largest_numbers.append(i)

print("List a = ", a)
print("list of indices for the largest numbers = ", largest_numbers)