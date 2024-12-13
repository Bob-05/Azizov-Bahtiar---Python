# Даны положительные числа A, B, C. На прямоугольнике размера A х B размещено
# максимально возможное количество квадратов со стороной C (без наложений).
# Найти количество квадратов, размещенных на прямоугольнике.
# Операции умножения и деления не использовать.

def check (type_string):
    value = input(type_string)

    while type(value) != int:
        try:
            value = int(value)
            if type(value) == int:
                return value
        except ValueError:
            print("TypeError!!!")
            value = input(type_string)


number_A = 0
number_B = 0
number_C = 0
