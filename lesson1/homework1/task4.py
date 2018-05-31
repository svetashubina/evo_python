#Вывести на экран любые две цифры из символов *
for i in range (1,7):
  if i == 1:
    print ('*'*6)
  elif i==6:
    print ('*'*6)
  else:
    print ('*'+'    '+'*')


for i in range (1,7):
  if i == 2:
    print (' '*4+'*'*2)
  elif i ==3:
    print (' '*3+'*'+' '+'*')
  else:
    print (' '*5+'*')
