#Дан массив целых чисел. Нужно найти сумму элементов с четными индексами (0-й, 2-й, 4-й итд),
# затем перемножить эту сумму и последний элемент исходного массива.
#Не забудьте, что первый элемент массива имеет индекс 0.
#Для пустого массива результат всегда 0 (ноль).
#Входные данные: Список (list) целых чисел (int).
#Выходные данные: Число как целочисленное (int).


def func(a):
    a = list(a)
    return sum(a[0::2]) * a[-1]

print(func([1,2,3]))


