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
    number = float(input(f"Введите число {i + 1}: "))
    numbers.append(number)


for num in numbers:
    B, C, D = PowerA234(num)
    print(f"Число: {num}, Вторая степень: {B}, Третья степень: {C}, Четвертая степень: {D}")
