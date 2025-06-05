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
                      (5, 'Вода газированная', 'Лента', 893, 207, 'литр', '27руб/литр'),
                      (6, 'Хлеб белый', 'Пятёрочка', 456, 1500, 'штука', '45руб/штука'),
                      (7, 'Яйца', 'Магнит', 789, 3000, 'десяток', '95руб/десяток'),
                      (8, 'Сахар', 'Лента', 321, 1200, 'кг', '65руб/кг'),
                      (9, 'Соль', 'Пятёрочка', 654, 1800, 'кг', '30руб/кг'),
                      (10, 'Масло подсолнечное', 'Магнит', 987, 900, 'литр', '150руб/литр')
                      ]
    cur.executemany("INSERT INTO items VALUES (?, ?, ?, ?, ?, ?, ?)", info_for_table)

    #cur.execute("SELECT * FROM items WHERE name_shop = 'Пятёрочка'")
    #print(cur.fetchall())
    #cur.execute("SELECT * FROM items WHERE CAST(SUBSTR(trade_price, 1, INSTR(trade_price, 'руб')-1) AS INTEGER) > 100")
    #print(cur.fetchall())
    #cur.execute("SELECT * FROM items WHERE unit_measure = 'литр' AND number_item > 2000")
    #print(cur.fetchall())

    #cur.execute("DELETE FROM items WHERE order_shop < 500")
    #cur.execute("DELETE FROM items WHERE name_shop = 'Магнит'")
    #cur.execute("DELETE FROM items WHERE number_item < 300")

    #cur.execute("UPDATE items SET trade_price = '130руб/литр' WHERE name_item = 'Молоко'")
    #cur.execute("UPDATE items SET number_item = number_item + 100 WHERE name_item = 'Вода питьевая'")
    #cur.execute("UPDATE items SET name_shop = 'Ашан' WHERE order_shop BETWEEN 800 AND 900")

    print(cur.rowcount)
