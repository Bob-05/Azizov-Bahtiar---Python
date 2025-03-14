"""
Средствами языка Python сформировать текстовый файл (.txt), содержащий
последовательность из целых положительных и отрицательных чисел.
Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:

Исходные данные:
Количество элементов:
Отрицательные нечетные элементы:
Сумма отрицательных нечетных элементов:
Среднее арифметическое отрицательных нечетных элементов:
"""


# функции для удобства
def integer(counter):
    integer_list = list()
    for i in range(counter):
        try:
            int_user = int(input("Введите отрицательное/положительное число: "))
            str_user = str(int_user)
            # print(int_user)
            integer_list.append(str_user)

        except ValueError:
            print("Неверный ввод!!!")
    return integer_list


def check(type_string):
    value = input(type_string)

    while type(value) != int:
        try:
            value = int(value)
            if type(value) == int:
                return value
        except ValueError:
            print("Введите целое число!!!")
            value = input(type_string)

def

# основной код программы
counter_us = check("Введите количество символов: ")
negative_num = -1
sum_negative_num = sum(x for x in counter_us if x < 0 and not x % 2 == 0)

f1 = open("my_one_file.txt", 'w')
f1.writelines(str(integer(counter_us)))

print(f"Исходные данные --> \033[1;32m{counter_us}\033[0;37m", file=f1)
print(f"Отрицательные нечётные элементы: {negative_num}", file=f1)
print(f"Сумма отрицательных нечетных элементов: \033[1;32m{sum_negative_num}", file=f1)
print(f"", file=f1)

f1.close()
