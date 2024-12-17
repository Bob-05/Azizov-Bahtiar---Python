# Даны три целых числа.
# Определить у какого числа больше сумма цифр.
# Вывод результата предусмотреть в основной программе.
# Расчет суммы цифр оформить в функции.



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

A = check('Enter the number A: ')
B = check('Enter the number B: ')
C = check('Enter the number C: ')

if sum_of_digits(A) > sum_of_digits(B) > sum_of_digits(C):
    print("The number A has the largest sum of digits!")
elif sum_of_digits(A) < sum_of_digits(B) > sum_of_digits(C):
    print("The number B has the largest sum of digits!")
else:
    print("The number C has the largest sum of digits!")