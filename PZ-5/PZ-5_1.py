
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


def sum_of_digits(n):
    n = abs(n)
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

def aspiration_to_zero(user_dg):
    limit = 0
    while user_dg > 0:
        user_dg -= sum_of_digits(user_dg)
        limit +=1
    return limit

input_digit = check('Enter digit: ')
input_digit = aspiration_to_zero(input_digit)
print("The number of steps to reach zero: ", input_digit)