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

rectangle_area = 0

# print("----")

while True:
    if number_B > 0:
        rectangle_area += number_A
        number_B -= 1
    else:
        break

square_area = 0

# print("----")

limits = number_C
while True:
    if limits > 0:
        square_area += number_C
        limits -= 1
    else:
        break

number_squares = 0;

# print("----")

while True:
    if rectangle_area > 0:
        number_squares += 1
        rectangle_area -= square_area
    else:
        break

print('Number of squares placed on a rectangle = ', number_squares)