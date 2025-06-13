"""
 Известно, что X кг конфет стоит A рублей.
 Определить, сколько стоит 1 кг и Y кг этих же конфет.
"""

import tkinter as tk
from tkinter import messagebox


def calculate():
    try:
        x = float(entry_x.get())
        a = float(entry_a.get())
        y = float(entry_y.get())

        if x <= 0 or a <= 0:
            messagebox.showerror("Ошибка", "X и A должны быть больше 0")
            return

        price = a / x
        result_1.config(text=f"1 кг = {price:.2f} руб")
        result_2.config(text=f"{y} кг = {price * y:.2f} руб")

    except:
        messagebox.showerror("Ошибка", "Введите числа")


# Создание окна
window = tk.Tk()
window.title("Стоимость конфет")
window.geometry("300x250")

# Поля ввода
tk.Label(window, text="X (кг):").pack()
entry_x = tk.Entry(window)
entry_x.pack()

tk.Label(window, text="A (руб):").pack()
entry_a = tk.Entry(window)
entry_a.pack()

tk.Label(window, text="Y (кг):").pack()
entry_y = tk.Entry(window)
entry_y.pack()

# Кнопка
tk.Button(window, text="Рассчитать", command=calculate).pack(pady=10)

# Результаты
result_1 = tk.Label(window, text="1 кг = ")
result_1.pack()

result_2 = tk.Label(window, text="Y кг = ")
result_2.pack()

window.mainloop()