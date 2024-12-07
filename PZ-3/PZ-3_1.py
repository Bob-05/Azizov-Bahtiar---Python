# Дано целое число A.
# Проверить истинность высказывания: число A является положительным.

digit = input("Enter digit a: ")

while type(digit) != int:
    try:
        digit = int(digit)
    except ValueError:
        print ("Enter int!!!")
        digit = input("Enter digit a: ")

if digit > 0:
    print('The number A is positive!!!')
else:
    print('The number A is not positive!!!')

