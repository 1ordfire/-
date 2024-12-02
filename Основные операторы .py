n = int(input('Введите целое число от 3 до 20: '))
def get_password(number):
    password = ''
    if number < 3:
        print("Ошибка. Введите целое число от 3 до 20")
    if number > 20:
        print("Ошибка. Введите целое число от 3 до 20")
    else:
        for i in range(1, number):
            for j in range(2, number):
                if j <= i:
                    continue
                if number % (i + j) == 0:
                    password += str(i) + str(j)
        return password


result = get_password(n)
print(result)
