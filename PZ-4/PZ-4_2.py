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


number_A = check('Enter number A: ')
number_B = check('Enter number B: ')
number_C = check('Enter number C: ')

Rectangle_area = 0

while True:
    if number_B > 0:
        Rectangle_area += number_A
        number_B -= 1
    else:
        break

Square_area = 0

while True:
    limits = number_C
    if limits > 0:
        Square_area += number_C
        limits -= 1
    else:
        break

number_squares = 0;

while True:
    if Rectangle_area > 0:
        number_squares += 1
        Rectangle_area -= Square_area
    else:
        break

print('Number of squares placed on a rectangle = ', number_squares)