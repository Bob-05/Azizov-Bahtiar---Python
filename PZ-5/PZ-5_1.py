
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
    counter = 0
    new_digit = 0
    while True:
        number = 10
        while user_dg % number >= 0 :
            new_digit += new_digit % number
            number *= 10
            print("...")
        user_dg = new_digit
        new_digit = 0
        print("...")
        counter += 1
        if user_dg % number < 0:
            return counter

print ("Number of actions = ", aspiration_to_zero(user_digit))