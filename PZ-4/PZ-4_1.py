# Даны два целых числа A и B (A < B).
# Вывести в порядке возрастания все целые числа,
# расположенные между A и B (включая сами числа A и B), а также количество этих чисел.

def check(digit):
    value = input(digit)

    while type(value) != int:
        try:
            value = int(value)
            if type(value) == int:
                if value > 0:
                    return value
        except ValueError:
            print("Enter a digit!!!")
            value = input(digit)


while True:
    number_A = check('Enter number A: ')
    number_B = check('Enter number B: ')
    if number_A > number_B:
        break
    else:
        print('Error - incorrect input!!!')

number_N = number_A

while True:
    print("--", number_N)
    number_N += 1
    if number_N > number_B:
        break

print("Number of whole numbers between", number_A, "and ", number_B, " = ", number_N)