#Дано пятизначное число. Цифры на четных позициях занулить. Например, из 12345 получается число 10305.

a = list(input('Введите пятизначное число: '))
for i in range(len(a)):
  if i % 2 != 0:
    a[i] = 0
print (''.join(a))

