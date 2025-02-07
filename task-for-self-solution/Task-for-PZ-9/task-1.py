"""
Дана строка «Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4».
Преобразовать информацию из строки в словарь, найти среднее арифметическое оценок, результаты вывести на экран.
"""

string_user = "Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4"
string_name = ''
list_score = list()


for index, value in enumerate(string_user):
        if type(value) == str:
            string_name += value

        elif type(value) == int and len(string_name) > index +1 and int(type(string_name[index+1]) == int):
            string_name += value
            string_name += string_name[index + 1]
        else:
            list_score += value

print(f"--string---> {string_name}")
print(f"--list-----> {list_score}")