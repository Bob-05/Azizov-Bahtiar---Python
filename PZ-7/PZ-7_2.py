"""
Дана строка, содержащая латинские буквы и скобки трех видов: «()», «[]», «{}».
Если скобки расставлены правильно (то есть каждой открывающей соответствует
закрывающая скобка того же вида), то вывести число 0. В противном случае вывести
или номер позиции, в которой расположена первая ошибочная скобка, или, если
закрывающих скобок не хватает, число —1
"""
def check_for_my_symbol(a):
    list_my_symbol = ['(',')','{','}','[',']']
    list_user_symbol = str()
    for i in a:
        for j in list_my_symbol:
            if i == j:
                list_user_symbol += i

    return list_user_symbol



string_user = str(input("Введите текст: "))
print(type(string_user), " " , check_for_my_symbol(string_user))

#for elem in string_user:
