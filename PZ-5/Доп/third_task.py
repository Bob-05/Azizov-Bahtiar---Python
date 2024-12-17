# Написать программу, подсчитывающую количество цифр числа, используя для этого функцию.



def sum_of_digits(n):
    n = abs(n)
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

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

number_a = check('Enter the number A: ')
print("The sum of the numbers of a given number = ", sum_of_digits(number_a))