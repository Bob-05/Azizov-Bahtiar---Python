"""
Приложение ОПТОВАЯ БАЗА для автоматизированного контроля движения
товаров на оптовой базе. Таблица Товары должна содержать следующие данные: Код
товара, Наименование товара, Наименование магазина, Заявки магазина, Количество
товара на складе, Единицы измерения, Оптовая цена.
"""

import sqlite3 as sq


with sq.connect('base.db') as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS items")
    cur.execute("""CREATE TABLE IF NOT EXISTS items(
        id_item int PRIMARY KEY,
        name_item text NOT NULL,
        name_shop text NOT NULL,
        order_shop int NOT NULL,
        number_item int NOT NULL,
        unit_measure text NOT NULL,
        trade_price text NOT NULL
        )
        """)

    info_for_table = [(1, 'Молоко', 'Пятёрочка', 100, 2500, 'литр', '120руб/литр'),
                      (2, 'Кефир', 'Пятёрочка', 900, 2809, 'литр', '110руб/литр'),
                      (3, 'Кола', 'Магнит', 1321, 1409, 'литр', '190руб/литр'),
                      (4, 'Вода питьевая', 'Лента', 895, 205, 'литр', '20руб/литр'),
                      (5, 'Вода газированая', 'Лента', 893, 207, 'литр', '27руб/литр'),
                      ]
    cur.executemany("INSERT INTO services VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", info_for_table)

    cur.execute("SELECT * FROM items")
    # print(cur.fetchall())
    # cur.execute("SELECT * FROM ")
    # print(cur.fetchall())
    # cur.execute("SELECT * FROM ")
    # print(cur.fetchall())

