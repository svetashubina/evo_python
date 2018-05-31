#Написать мини-калькулятор, который бы слаживал и вычитал числа. И возводил в степень. ( То есть вы передаете скрипту два числа и оператор минус или плюс или возведения в степень)
a = int(input('Print first number: '))
b = int(input('Print second number: '))
operator = (input('Print operator +/-/**: '))

if operator == '+':
  print (a+b)
elif operator =='-':
  print (a-b)
else:
  print (a**b)
