"""
Дана строка, содержащая латинские буквы и скобки трех видов: «()», «[]», «{}».
Если скобки расставлены правильно (то есть каждой открывающей соответствует
закрывающая скобка того же вида), то вывести число 0. В противном случае вывести
или номер позиции, в которой расположена первая ошибочная скобка, или, если
закрывающих скобок не хватает, число —1
"""


def check_parentheses(s):
    open_brackets = "([{"
    close_brackets = ")]}"
    stack = ""

    for index in range(len(s)):
        char = s[index]
        if char in open_brackets:
            stack += char
        elif char in close_brackets:
            if not stack:
                return index + 1
            last_open = stack[-1]
            if (last_open == '(' and char == ')') or (last_open == '[' and char == ']') or (last_open == '{' and char == '}'):
                stack = stack[:-1]
        else:
            return index + 1


    if stack:
        return -1
    # всё верно
    return 0

string_user = str(input("Enter the string: "))
print(f"Лог программы: {check_parentheses(string_user)}")
