# Известно, что X кг конфет стоит A рублей;
# Определить, сколько стоит 1 кг и Y кг этих же конфет.

number_candies_old = int(input('Введите текущее количество конфет: '))
cost_candy_old = int(input('Введите общую стоимость конфет: '))

cost_one_candy = number_candies_old / cost_candy_old
number_candies_new = int(input('Введите новое количество конфет: '))
cost_candy_new = number_candies_new + cost_one_candy
print("Стоимость", number_candies_new, "конфет = ", cost_candy_new)
