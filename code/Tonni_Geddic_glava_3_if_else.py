#!/usr/bi/env python3
# -*- coding: utf-8 -*-
#*****************************************************************************************************
# Задание № 1. 
# Напишите инструкцию if, которая присваивает значение 20 переменной у и значение 40 
# переменной z,  если переменная х больше 100.
#print('*'*70)
#x = int(input('Введите значение переменной х: '))
#y = 0
#z = 0
#if x > 100:
    #y = 20
    #z = 40
#print(f'y = {y} z = {z}')
#print('*'*70) 
#*********************************************************************************************************
# Задание № 3. 
# Напишите инструкцию if-else,  которая присваивает значение О переменной ь,  если 
# переменная а меньше 1О . В противном случае она должна присвоить переменной ь значе­ние 99. 
#print('*'*70)
#a = int(input('Введите значение переменной a: '))
#if a < 10:
    #b = 0
#else:
    #b = 99
#print(f'b = {b}')
#print('*'*70)

#**********************************************************************************************************
# Задание № 5. 
# Напишите вложенные структуры принятия решения, которые выполняют следующее: 
# если amountl больше 10 и amount2 меньше 100, то показать большее значение из двух пе­ременных amountl и amount2.
#print('*'*70)
#amount1 = int(input('Введите значение переменной amount1: '))
#amount2 = int(input('Введите значение переменной amount2: '))
#if amount1 > 10 and amount2 < 100:
    #if amount1 < amount2:
        #print(amount2)
    #else:
        #print(amount1)
#print('*'*70)
#***********************************************************************************************************
# Задание № 6.
# Напишите инструкцию if-else,  которая выводит сообщение  'Скорость  нормальная', 
# если переменная speed находится в диапазоне от 24  до 56.  Если значение переменной 
# speed лежит вне этого диапазона, то показать 'Скорость  аварийная'.
#print('*'*70)
#speed = int(input('Введите значение скорости: ' ))
#if 24 < speed < 56:
    #print('Скорость  нормальная')
#else:
    #print('Скорость  аварийная')
#print('*'*70)
#***************************************************************************************************************
#***************************************************************************************************************
# Задание № 1. День недели. 
# Напишите программу, которая запрашивает у пользователя число в диапа­зоне от  1  до 7. 
# Эта программа должна показать соответствующий день недели, где 
# l - понедельник, 2 - вторник, 3 - среда, 4 - четверг, 5 - пятница, 6 - суббота и 7 - воскресенье. 
# Программа должна вывести сообщение об ошибке, если пользователь 
# вводит номер, который находится вне диапазона от 1 до 7.
#print('*'*70)
#item = int(input('Введите число от 1 до 7: '))
#if 1 < item > 7:
    #print('Введеное число не входит в заданный диапазон')
#if item == 1:
    #print('понедельник')
#elif item == 2:
    #print('вторник')
#elif item == 3:
    #print('среда')
#elif item == 4:
    #print('четверг')
#elif item == 5:
    #print('пятница')
#elif item == 6:
    #print('суббота')
#elif item == 7:
    #print('воскресенье')    
#print('*'*70)

# Задание 2. Площади прямоугольников.  
# Площадь прямоугольника - это произведение его длины на его ширину. 
# Напишите программу, которая запрашивает длину и ширину двух прямо­угольников. 
# Программа должна выводить пользователю сообщение о том, площадь како­го прямоугольника 
# больше, либо сообщать, что они одинаковы. 
#print('*'*70)
#dlina1 = int(input('Введите длину первого прямоугольника: '))
#shirina1 = int(input('Введите ширину первого прямоугольника: '))

#dlina2 = int(input('Введите длину второго прямоугольника: '))
#shirina2 = int(input('Введите ширину второго прямоугольника: '))

#s1 = dlina1*shirina1
#s2 = dlina2*shirina2
#if s1 == s2:
    #print('Площади прямоугольников одинаковы.')
#elif s1 < s2:
    #print('Площадь второго прямоугольника больше.')
#else:
    #print('Площадь первого прямоугольника больше.')   
#print('*'*70)

# Задание 3. Классификатор возраста. 
# Напишите программу, которая просит пользователя ввести возраст человека. 
# Программа должна определить, к какой категории этот человек при­надлежит: младенец, 
# ребенок, подросток или взрослый, и вывести соответствующее со­общение. 
# Ниже приведены возрастные рекомендации: 
# •  если возраст 1 год или меньше, то он или она - младенец; 
# •  если возраст старше l года, но моложе 13 лет, то он или она- ребенок; 
# •  если возраст не менее 13 лет, но моложе 20 лет, то он или она - подросток; 
# •  если возраст более 20 лет, то он или она- взрослый.
#print('*'*70)
#age = float(input('Введите ваш возраст: '))
#if age <= 1:
    #print('младенец')
#elif age > 1 and age < 13:
    #print('ребенок')
#elif age >= 13 and age < 20:
    #print('подросток')
#elif age > 20:
    #print('взрослый')    
#print('*'*70)

# Задание 3.Римские цифры. 
# Напишите программу, которая предлагает пользователю ввести число в диапазоне от 1 до 10.  
# Программа должна показать для этого числа римскую цифру. 
# Если число находится вне диапазона 1 до 10, то программа должна вывести сообщение об ошибке. 
#print('*'*70)
#number = int(input('Введите число от 1 до 10: '))
#rim_number = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
#print('*'*70)
# первый способ
#for y, x in zip(rim_number, range(1, number+1)):
    #if x == number:
        #print(f'Латинская цифра {number} = римской цифре {y}.')
        
# второй способ
#if  number < 1 or number > 10:
    #print('Ошибка !!! Число должно быть больше или равно 1 и меньше или равно 10.')
#lat_rim = {
    #1:'I', 
    #2:'II', 
    #3:'III', 
    #4:'IV', 
    #5:'V', 
    #6:'VI', 
    #7:'VII', 
    #8:'VIII', 
    #9:'IX', 
    #10:'X'
#}
#for x, y in lat_rim.items():
    #if x == number:
        #print(f'Латинская цифра {number} = римской цифре {y}.')
#print('*'*70)

# Задание 4.Волшебные даты. 
#Дата 10 июня 1960 года является особенной, потому что если ее запи­сать в приведенном ниже формате,
#то произведение дня и месяца равняется году: 10.06.60 
#Разработайте программу, которая просит пользователя ввести месяц (в числовой форме), 
#день и двузначный год. Затем программа должна определить, равняется ли произведение 
#дня и месяца году. Если это так, то она должна вывести сообщение, говорящее, что вве­
#денная дата является волшебной. В противном случае она должна вывести сообщение, 
#что дата не является волшебной.
#print('*'*70)
#day = int(input('Введите день в числовой форме: '))
#mounce = int(input('Введите месяц в числовой форме: '))
#year = int(input('Введите год в числовой двузначной форме: '))
#if day*mounce == year:
    #print('дата является волшебной.')
#else:
    #print('дата не является волшебной.')
#print('*'*70)


# Задание 5.Калькулятор сосисок для пикника.

# Допустим, что сосиски упакованы в пакеты по 10 штук, а булочки - в пакеты по 8  штук. 
# Напишите программу, которая вычисляет количество упаковок с сосисками и количество упаковок с булочками, 
# необходимых для пикника с минимальными остатками. Программа должна запросить у пользователя коли­чество 
# участников пикника и количество хот-догов, которые будут предложены каждому участнику. 
# Программа должна показать приведенные ниже подробности: 
# •  минимально необходимое количество упаковок с сосисками; 
# •  минимально необходимое количество упаковок с булочками; 
# •  количество оставшихся сосисок; 
# •  количество оставшихся булочек. 

#print('*'*70)
#people = int(input('Введите количество участников пикника: '))
#xot_gog = int(input('Введите количество хот догов для каждого участника: '))
#sosige = 10
#bread = 8
#print(f'Минимально необходимое количество упаковок с сосисками: {(people*xot_gog)//sosige} штук.')
#print(f'Минимально необходимое количество упаковок с булочками: {(people*xot_gog)//bread} штук.')
#print(f'количество оставшихся сосисок: {(people*xot_gog)%sosige} штук.')
#print(f'количество оставшихся булочек: {(people*xot_gog)%bread} штук.')
#print('*'*70)

# Задание 6.Цвета колеса рулетки. 
#Цвета колеса рулетки. На колесе рулетки карманы пронумерованы от О до 36.  Ниже приведены цвета карманов: 
#•  карман О- зеленый; 
#•  для карманов с 1 по 1О карманы с нечетным номером имеют красный цвет, карманы 
#с четным номером - черный; 
#•  для карманов с 11  по 18  карманы с нечетным номером имеют черный цвет, карманы 
#с четным номером - красный; 
#•  для карманов с 19  по 28  карманы с нечетным номером имеют красный цвет, карманы 
#с четным номером - черный; 
#•  для карманов с 29  по 36 карманы с нечетным номером имеют черный цвет, карманы 
#с четным номером - красный. 
#Напишите программу, которая просит пользователя ввести номер кармана и показывает, 
#является ли этот карман зеленым, красным или черным. Программа должна вывести 
#сообщение об ошибке, если пользователь вводит число, которое лежит вне диапазона 
#ОТ 0 ДО 36. 

#print('*'*70)
#position = int(input('Введите номер позиции на барабане рулетки: '))
#if  position < 0 or position > 36:
    #print('Ошибка !!! Число должно быть больше или равно 1 и меньше или равно 36.')
#if position == 0:
    #print('Это карман является ЗЕЛЕНЫМ.')
#elif (position >= 1 and position <= 10) and position%2 == 0:
    #print('Это карман является ЧЕРНЫМ.')
#elif (position >= 1 and position <= 10) and position%2 != 0:
    #print('Это карман является КРАСНЫМ.')
#elif (position >= 11 and position <= 18) and position%2 == 0:
    #print('Это карман является КРАСНЫМ.')
#elif (position >= 11 and position <= 18) and position%2 != 0:
    #print('Это карман является ЧЕРНЫМ.')
#elif (position >= 19 and position <= 28) and position%2 == 0:
    #print('Это карман является ЧЕРНЫМ.')
#elif (position >= 19 and position <= 28) and position%2 != 0:
    #print('Это карман является КРАСНЫМ.')
#elif (position >= 29 and position <= 36) and position%2 == 0:
    #print('Это карман является КРАСНЫМ.')
#elif (position >= 29 and position <= 36) and position%2 != 0:
    #print('Это карман является ЧЕРНЫМ.')    
#print('*'*70)


# Задание 6.Цвета колеса рулетки. 
print('*'*70)

print('*'*70)
print('END')
