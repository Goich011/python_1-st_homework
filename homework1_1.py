#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#Пример:
#- 6 -> да
#- 7 -> да
#- 1 -> нет

a = int(input('Введи цифру дня недели а я напишу является ли он выходным днем:  \n'))

while a < 1 or a > 7:
    a = int(input('Эта цифра не является днем недели. Цифры дней недели от 1 до 7, введи новую цифру:  \n'))

if a >= 1 and a <= 5:
    print('Нет')
if a >= 6 and a <= 7:
    print('Да')

#if a == 1:
#    print('Понедельник')
#if a == 2:
#    print('Вторник')
#if a == 3:
#    print('Среда')
#if a == 4:
#    print('Четверг')
#if a == 5:
#    print('Пятница')
#if a == 6:
#    print('Суббота')
#if a == 7:
#    print('Воскресенье')