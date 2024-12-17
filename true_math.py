def divide():
    first = int(input("Введите число для деления:"))
    second = int(input("Введите число на которое хотите поделить('На ноль делить можно'):"))
    if second == 0:
       positive_infinity = float('inf')
       print(positive_infinity)
    else:
       c = first / second
       print(c)