# Используя словарь посчитать количество уникальных слов в заданном предложении «Изучаем язык Питон».
# Вывести на экран каждую пару «ключ:значение».


string = input("Введите текст: ")
list_string = string.split()
value_dict = dict()
counter_keys = 0

for i in list_string:
    if i not in value_dict:
        value_dict[i] = 1
        counter_keys += 1
    else:
        value_dict[i] += 1

print("Количество повторений уникальных слов:")
for i in value_dict.items():
    print(i)

print(f"Количество уникальных слов: {counter_keys}")
