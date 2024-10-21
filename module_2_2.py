fist=input('Введите первое число: ')
second=input('Введите второе число: ')
third=input('Введите третье число')
if fist==second==third:
    print(3)
elif fist==second or fist==third or second==third:
    print(2)
else:
    print('Равных чисел нет')