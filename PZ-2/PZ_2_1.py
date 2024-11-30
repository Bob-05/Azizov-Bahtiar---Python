# Известно, что X кг конфет стоит A рублей;
# Определить, сколько стоит 1 кг и Y кг этих же конфет.

def get_positive_int(promt):
    while True:
        try:
            value = int(input(promt))
            if value > 0:
                return value
            else:
                print ("Enter a number greater than zero.")

        except ValueError:
            print("Incorrect input!!! Enter a positive integer")


# Получаем данные от пользователя
weight_candies_old = get_positive_int('Enter the weight of the candies in kilograms: ')
cost_candy_old = float(input('Enter the cost in rubles: '))

# Рассчитываем стоимость одного килограмма конфет
cost_one_kilogram = cost_candy_old / weight_candies_old

weight_candies_new = get_positive_int('Enter the new candy weight: ')
cost_candy_new = weight_candies_new * cost_one_kilogram

# Выводим результаты
print("The cost of one kilogram of sweets =", cost_one_kilogram)
print("Cost", weight_candies_new, "kg of sweets =", cost_candy_new, "in rubles.")
