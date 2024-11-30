# Известно, что X кг конфет стоит A рублей;
# Определить, сколько стоит 1 кг и Y кг этих же конфет.

number_candies_old = int(input('Enter the number of candies: '))
while type(number_candies_old) != int:
    try:
        number_candies_old = int(number_candies_old)
    except ValueError:
        print("Invalid input!!!")
        number_candies_old = int(input('Enter an integer: '))

cost_candy_old = float(input('Enter the total cost of candies:'))
while type(cost_candy_old) != int:
    try:
        cost_candy_old = int(cost_candy_old)
    except ValueError:
        print("Invalid input!!!")
        cost_candy_old = int(input('Enter an integer: '))


# How much does one kg of sweets cost?
cost_one_candy = float(number_candies_old / cost_candy_old)

number_candies_new = int(input('Enter the new number of candies: '))
while type(number_candies_new) != int:
    try:
        number_candies_new = int(number_candies_new)
    except ValueError:
        print("Invalid input!!!")
        number_candies_new = int(input('Enter an integer: '))

cost_candy_new = number_candies_new + cost_one_candy
print("Cost", number_candies_new, "of candy = ", cost_candy_new)
