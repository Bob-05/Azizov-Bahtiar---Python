# Дан символ C.
# Вывести его код (то есть номер в кодовой таблице).

symbol_user = input("Введите символ: ")

if len(symbol_user) > 1:
    print("символ - код")
    for i in range(len(symbol_user)):
        print(f"    {symbol_user[i]} -> {ord(symbol_user[i])}")
else:
    print(ord(symbol_user))
