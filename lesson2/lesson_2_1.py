a = int(input('Введите число: '))
if a > 10:
    print(a)
elif 0 < a < 5:
    if a + 11 > 13:
        print('Стало больше 13')
    else:
        print(a)
else:
    if (a - 100) > -200 and (a - 100)< -50:
        print('-200,-50 {}'.format(a))
    else:
        print('{} Что-то пошло на право'.format(a))