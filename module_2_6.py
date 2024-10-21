def get_password(number):
    password = ""
    for i in range (1, number):
        for j in range (2, number):
            if j > i:
                if j <= 1:
                    continue
                if number % (i + j) == 0:
                     password += str (i) + str (j)
    return password
n = int (input ('Введите число 3 до 20: '))
result = get_password (n)
print ('Пароль: ', result)