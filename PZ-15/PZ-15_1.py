"""
Приложение ОПТОВАЯ БАЗА для автоматизированного контроля движения
товаров на оптовой базе. Таблица Товары должна содержать следующие данные: Код
товара, Наименование товара, Наименование магазина, Заявки магазина, Количество
товара на складе, Единицы измерения, Оптовая цена.
"""

import sqlite3 as sq
import msvcrt
import time


def non_blok_input():
    position_cur = 3
    print(f"\033[{position_cur};1H\033[1;31m>\033[0;37m")  # Начальная позиция

    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'\xe0' or key == b'\x00':  # Проверка на спецклавиши
                key = msvcrt.getch()

                # Очищаем предыдущую позицию
                print(f"\033[{position_cur};1H ", end='', flush=True)

                if key == b'H' and position_cur > 3:  # Стрелка вверх
                    position_cur -= 1
                elif key == b'P' and position_cur < 6:  # Стрелка вниз
                    position_cur += 1
                else:
                    print("\a")

                # Рисуем новый указатель
                print(f"\033[{position_cur};1H\033[1;31m>\033[0;37m", end='', flush=True)
            elif key == b'\r':  # enter
                print(f"\033[8;1H ", end='', flush=True)
                return position_cur - 3
            else:
                print("\a")




with sq.connect('base.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS items(
        id_item int PRIMARY KEY,
        name_item text NOT NULL,
        name_shop text NOT NULL,
        order_shop text NOT NULL,
        number_item int NOT NULL,
        unit_measure text NOT NULL,
        trade_price int NOT NULL
        )
        """)


print("\033[1;33mПрограмма-\"ОПТОВАЯ БАЗА\" для взаимодействия с БД магазина!\033[0;37m")
print("\033[1;35mДоступные функции:\033[0;34m")
func_prog_list = ["Поиск данных", "Удаление данных", "Редактирование данных", "Загрузить свой скрипт"]
for elem in func_prog_list:
    print(" ",elem)

number_f = non_blok_input()
print(f"\033[0;37mВы выбрали \033[1;34m{func_prog_list[number_f]}\033[0;37m")
input("Нажмите Enter для выхода...")

print("\033[H\033[J", end='', flush=True)  # Очищает экран и ставит курсор в начало

if number_f == 0:
    while True:
        with sq.connect('base.db') as con:
            cur = con.cursor()
            cur.execute("""DESCRIBE items;""")
            result = cur.fetchall()
            print(result)




if number_f == 1:
    """..."""
if number_f == 2:
    """..."""
if number_f == 3:
    """..."""


input("Нажмите Enter для выхода...")

