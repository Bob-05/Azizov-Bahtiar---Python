# Описать функцию PowerA234(параметры), вычисляющую вторую, третью и
# четвертую степень числа A и возвращающую эти степени соответственно в переменные B, C и D.
# С помощью этой функции найти вторую, третью и четвертую степень пяти данных чисел.


def check(type_string) -> object:
    value = input(type_string)

    while type(value) != float:
        try:
            value = float(value)
            if type(value) == float:
                return value
        except ValueError:
            print("TypeError!!!")
            value = input(type_string)

def PowerA234(A):
    B = A ** 2
    C = A ** 3
    D = A ** 4
    return B, C, D

# Список для хранения чисел
numbers = []

for i in range(5):
    number = check(f"Enter a number {i + 1}: ")
    numbers.append(number)


for num in numbers:
    B, C, D = PowerA234(num)
    print(f"Number: {num}, Second degree: {B}, Third degree: {C}, Fourth degree: {D}")
