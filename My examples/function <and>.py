
print('Мне нужна ваша дата рождения в формате "дд.мм.гггг"')
print('Введите ДЕНЬ по номеру?')
a = int(input())
print('Введите МЕСЯЦ по номеру?')
b = int(input())
print('Введите ГОД по номеру?')
c = int(input())


if 0 < a < 32 and 0 < b < 13 and 1900 < c < 2022 :
  print('Спасибо! Теперь я знаю вашу дату рождения',a,'.',b,'.',c,'г.')
else:
  print('Извините но вы некорректно указали одно или несколько значений, попробуйте снова')

print('Введите ДЕНЬ по номеру?')
a = int(input())
print('Введите МЕСЯЦ по номеру?')
b = int(input())
print('Введите ГОД по номеру?')
c = int(input())


if 0 < a < 32 and 0 < b < 13 and 1900 < c < 2022 :
  print('Спасибо! Теперь я знаю вашу дату рождения',a,'.',b,'.',c,'г.')
else:
  print('Уф я с вами замучился, идите в баню!!!')
