# Даны два целых числа A и B (A < B).
# Вывести в порядке возрастания все целые числа,
# расположенные между A и B (включая сами числа A и B),
# а также количество этих чисел.

def check(digit):
    value = input(digit)

    while type(value) != float:
        try:
            value = float(value)
            if (type(value) == float):
                return value
        except:
            print("Enter a digit!!!")
            value = input(digit)


while True:
    number_A = check('Enter number A: ')
    number_B = check('Enter number B: ')
    if number_A > number_B:
        break
    else:
        print('Error - incorrect input!!!')

