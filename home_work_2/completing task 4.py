print('К А Л Ь К У Л Я Т О Р')

while True:

  symbol = input('Введите знак (+,-,*,/ или 0 для завершения):  ')
  a= float(input('введите первое число:   '))
  b= float(input('введите второе число:   '))
  
  if symbol == '0':
    print('вычисления завершены')
  
    break
  if symbol in ('+','-','*','/'):
    if symbol == '+':
      print(a+b)
    elif symbol == '-':
      print(a-b)
    elif symbol == '*':
      print(a*b)
    elif symbol == '/':
      print(a/b)
    elif symbol == '/':
      if b != 0:
        print('на Ноль не делится!')
      
  else:
    print ('повторите знак операции!')
