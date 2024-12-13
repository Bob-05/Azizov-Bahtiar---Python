# Даны два целых числа A и B (A < B).
# Вывести в порядке возрастания все целые числа,
# расположенные между A и B (включая сами числа A и B), а также количество этих чисел.

def check(type_string):
    value = input(type_string)

    while type(value) != int:
        try:
            value = int(value)
            if type(value) == int:
                return value
        except ValueError:
            print("Enter a digit!!!")
            value = input(type_string)

number_A = 0
number_B = 0

while True:
    number_A = check('Enter number A: ')
    number_B = check('Enter number B: ')
    print(type(number_B))
    if number_A < number_B:
        break
    else:
        print('Error - incorrect input!!! (A < B)')

number_N = number_A

while True:
    print("--", number_N)
    number_N += 1
    if number_N > number_B:
        break

print("Number of whole numbers between", number_A, "and ", number_B, " = ", number_N)