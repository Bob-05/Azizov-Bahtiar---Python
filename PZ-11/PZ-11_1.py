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


def negative_int_s(str_file):
    int_neg = 0
    for i in len(str_file[0]):
        if int(str_file) < 0:
            int_neg += int(str_file)
    return int_neg




# основной код программы
counter_us = check("Введите количество символов: ")

f1 = open("my_one_file.txt", 'w')
f1.writelines(str(integer(counter_us)))
f1.close()

f1 = open("my_one_file.txt", 'r')
str_from_file = f1.readlines()
print(f"Исходные данные --> \033[1;32m{str_from_file}\033[0;37m")
print(f"Отрицательные нечётные элементы: ")
print(f"Сумма отрицательных нечетных элементов: \033[1;32m{negative_int_s(str_from_file)} \033[0;37m")
f1.close()
