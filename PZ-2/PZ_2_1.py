# Известно, что X кг конфет стоит A рублей;
# Определить, сколько стоит 1 кг и Y кг этих же конфет.

number_candies_old = int(input('Enter the number of candies:'))
cost_candy_old = float(input('Enter the total cost of candies:'))

cost_one_candy = float(number_candies_old / cost_candy_old)
number_candies_new = int(input('Enter the new number of candies:'))
cost_candy_new = number_candies_new + cost_one_candy
print("Cost", number_candies_new, "of candy = ", cost_candy_new)
