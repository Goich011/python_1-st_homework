#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#Пример:
#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3

print('Введи 2 числа, я согласно этим числам укажу в какой из четвертей графика находтся эта точка')
x = int(input('Введи число по оси X: \n'))
while x == 0:
    x = int(input('Введи число по оси X больше 0: \n'))
y = int(input('Введи число по оси Y: \n'))
while y == 0:
    y = int(input('Введи число по оси Y больше 0: \n'))

if x > 0 and y > 0:
    print('I четверть')
if x < 0 and y > 0:
    print('II четверть')
if x < 0 and y < 0:
    print('III четверть')
if x > 0 and y < 0:
    print('IV четверть')
