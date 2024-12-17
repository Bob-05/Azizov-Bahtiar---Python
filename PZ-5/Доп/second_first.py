# Рассчитать и вывести периметр и площадь прямоугольника.
# Расчеты оформить в функции.


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


def perimeter_area_rectangle (a = 0, b = 0):
    print("The perimeter of the rectangle = ", 2* a + b * 2)
    print("The area of the rectangle = ", a * b)


A = check("Enter the length of side 'a': ")
B = check("Enter the length of side 'b': ")

perimeter_area_rectangle(A, B)
