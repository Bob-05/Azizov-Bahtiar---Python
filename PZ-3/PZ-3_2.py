# Даны координаты точки, не лежащей на координатных осях OX и OY.
# Определить номер координатной четверти, в которой находится данная точка.

def check(digit):
    value = input(digit)

    while type(value) != float:
        try:
            value = float(value)
            if type(value) == float:
                return value
        except ValueError:
            print("Enter a digit!!!")
            value = input(digit)

axis_x = check('Enter coordinate axis X: ')
axis_y = check('Enter coordinate axis Y: ')

if axis_x > 0 and axis_y > 0:
    print('The point is in the first quarte!!!')

if axis_x > 0 > axis_y:
    print('The point is in the fourth quarter!!!')

if axis_x < 0 and axis_y < 0:
    print('The point is in the third quarter!!!')

if axis_x < 0 < axis_y:
    print('The point is in the second quarter!!!')
