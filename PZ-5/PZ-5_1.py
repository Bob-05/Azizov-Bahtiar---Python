
def check(type_string) -> object:
    value = input(type_string)

    while type(value) != float:
        try:
            value = float(value)
            if type(value) == float:
                return
        except ValueError:
            print("TypeError!!!")
            value = input(type_string)


user_digit = check('Enter digit: ')
def aspiration_to_zero(user_dg):
    number = 10
    new_digit = 0
    while user_dg > 0:
        new_digit += user_dg / number
        number *= 10


