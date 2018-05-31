i = 1
while i <= 5:
    pin = str(input('Введите пароль:'))
    print('your user {} attempt out of 5'.format(i))
    if pin == '1234':
        print('Доступ открыт')
        i = 6
    else:
        i += 1
        if i <= 5:
            print('Попробуй еще')
