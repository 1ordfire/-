def divide():
    first = int(input("Введите число для деления:"))
    second = int(input("Введите число на которое хотите поделить('На ноль делить нельзя'):"))
    if second == 0:
        print("Ошибка")
    else:
        c = first / second
        print(c)