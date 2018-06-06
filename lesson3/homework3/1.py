#Есть два игровых кубика с значениями от 1 до 6.
#Написать функцию, которая имитирует выбрасывание двух кубиков до тех пор
#пока сумма значений не будет равна 8.
#Когда сумма значений равна 8 - выводит значение каждого кубика и

from random import randint


def rand():
    n = 0
    while True:
            n = n + 1
            cub1 = randint(1, 6)
            cub2 = randint(1, 6)
            if cub2 + cub1 == 8:
                print(cub1)
                print(cub2)
                print(n)
                break
rand()

