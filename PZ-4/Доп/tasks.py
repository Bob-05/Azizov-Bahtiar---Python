# Задача 1: Ввести 4 числа. Найти и вывести на экран сумму и количество отрицательных чисел.
print("Задача 1")
negative_count = 0
negative_sum = 0
i = 0

while i < 4:
    try:
        number = float(input("Введите число: "))
        if number < 0:
            negative_count += 1
            negative_sum += number
        i += 1
    except ValueError:
        print("Ошибка ввода! Пожалуйста, введите числовое значение.")

print(f"Сумма отрицательных чисел: {negative_sum}")
print(f"Количество отрицательных чисел: {negative_count}\n")

# Задача 2: Ввести 4 числа. Найти и вывести на экран количество четных чисел.
print("Задача 2")
even_count = 0
i = 0

while i < 4:
    try:
        number = int(input("Введите число: "))
        if number % 2 == 0:
            even_count += 1
        i += 1
    except ValueError:
        print("Ошибка ввода! Пожалуйста, введите целое число.")

print(f"Количество четных чисел: {even_count}\n")

# Задача 3: Найти и вывести на экран квадраты и кубы чисел от 2 до 5.
print("Задача 3")
i = 2

while i <= 5:
    print(f"{i}^2 = {i ** 2}, {i}^3 = {i ** 3}")
    i += 1
print()

# Задача 4: Найти и вывести на экран S=1!+2!+3!+4!+…+n! (n>1).
def factorial(num):
    if num == 0 or num == 1:
        return 1
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result



# Основная программа
n = int(input("Введите n (n > 1): "))
if n <= 1:
    print("n должно быть больше 1.")
else:
    S = 0
    for i in range(1, n + 1):
        S += factorial(i)

    print(f"S = {S}")

# Задача 5: Ввести N чисел. Найти и вывести их среднее арифметическое.
print("Задача 5")
try:
    N = int(input("Введите количество чисел: "))
    total = 0
    i = 0

    while i < N:
        try:
            number = float(input("Введите число: "))
            total += number
            i += 1
        except ValueError:
            print("Ошибка ввода! Пожалуйста, введите числовое значение.")

    average = total / N
    print(f"Среднее арифметическое: {average}\n")
except ValueError:
    print("Ошибка ввода! Пожалуйста, введите целое число.\n")

# Задача 6: Ввести N чисел. Посчитать и вывести количество чисел равных нулю.
print("Задача 6")
try:
    N = int(input("Введите количество чисел: "))
    zero_count = 0
    i = 0

    while i < N:
        try:
            number = float(input("Введите число: "))
            if number == 0:
                zero_count += 1
            i += 1
        except ValueError:
            print("Ошибка ввода! Пожалуйста, введите числовое значение.")

    print(f"Количество нулей: {zero_count}\n")
except ValueError:
    print("Ошибка ввода! Пожалуйста, введите целое число.\n")

# Задача 7: Даны два целых числа А и В (А < В). Вывести в порядке убывания все целые числа, расположенные между А и В.
print("Задача 7")
try:
    A = int(input("Введите A (A < B): "))
    B = int(input("Введите B (A < B): "))

    if A >= B:
        raise ValueError("A должно быть меньше B.")

    count = B - A + 1
    while B >= A:
        print(B)
        B -= 1

    print(f"Количество чисел: {count}\n")
except ValueError as e:
    print(f"Ошибка ввода: {e}\n")

# Задача 8: Даны два целых числа А и В (А < В). Найти сумму всех целых чисел от А до В включительно.
print("Задача 8")
try:
    A = int(input("Введите A (A < B): "))
    B = int(input("Введите B (A < B): "))

    if A >= B:
        raise ValueError("A должно быть меньше B.")

    total_sum = 0
    while A <= B:
        total_sum += A
        A += 1

    print(f"Сумма от A до B: {total_sum}\n")
except ValueError as e:
    print(f"Ошибка ввода: {e}\n")

# Задача 9: Посчитать и вывести количество элементов арифметической прогрессии, удовлетворяющих условию 10 < ai < 30.
print("Задача 9")
a1 = 1
d = 3
count = 0
ai = a1

while ai < 30:
    if ai > 10:
        count += 1
    ai += d

print(f"Количество элементов: {count}\n")
