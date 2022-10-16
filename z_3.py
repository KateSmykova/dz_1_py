# Задача 3

x = int(input('Введите координату x: '))
y = int(input('Введите координату y: '))

if x>0 and y>0:
     print('Первая четверть')
if x<0 and y>0:
     print('Вторая четверть')
if x<0 and y<0:
     print('Третья четверть')
if x>0 and y<0:
     print('Четвертая четверть')
if x==0 or y==0:
     print('нет такой четверти')