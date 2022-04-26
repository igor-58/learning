#!usr/bin/env python3
# -*- coding: utf-8 -*-
#Напишите короткую программу, которая применяет цикл for для записи в файл чисел 
#от 1 до10.
#my_failes = open(r'D:\RPy222\test.txt', 'w')
#for item in range(1, 11):
    #my_failes.write(str(item) + ' ')
#my_failes.close()

#file = open(r'D:\RPy222\data.txt', 'w')
#file.write('Привет\n')
#file.write('Здорово\n') 
#file.write('Пока\n') 
#file.close()
# #######################################################################################
#Допустим, что существует файл data_1.txt,  который содержит несколько строк текста. 
#Напишите короткую программу с использованием цикла while, который показывает 
#все строки в файле. 

#file_reed = open(r'D:\RPy222\data_1.txt','r', encoding='UTF-8')
# с применением цикла while
#line = file_reed.readline()
#while line != '':
    #print(line.rstrip('\n'))
    #line = file_reed.readline()
#************************************************************************
# то же самое с применением цикла for
#for lines in file_reed:
    #print(lines.rstrip('\n'))
#file_reed.close()
# ###########################################################################################
#                        ЗАПИСЫВАЕМ В ФАЙЛ
#count_epms = int(input('Сколько записей о сотрудниках вы хотите создать? '))
#file_emps = open(r'D:\RPy222\ernployees.txt', 'w')
#for item in range(1, count_epms + 1):
    #print('Введите данные о сотруднике №  ', item, sep='')
    #name = input('Имя: ')
    #id_emps = input('Идентификационный номер: ')
    #dept  =  input('Отдел: ')
    #file_emps.write(name + '\n')
    #file_emps.write(id_emps + '\n')
    #file_emps.write(dept + '\n')
    #print()
#file_emps.close()
#        ЧИТАЕМ ИЗ ФАЙЛА
#file_emps = open(r'D:\RPy222\ernployees.txt', 'r')
#name = file_emps.readline()
#while name != '':
    #id_emps = file_emps.readline()
    #dept = file_emps.readline()
    #name = name.rstrip('\n')
    #id_emps = id_emps.rstrip('\n')
    #dept = dept.rstrip('\n')
    #print('Имя: ', name)
    #print('ИД: ', id_emps)
    #print('Отдел: ', dept)
    #print()
    #name = file_emps.readline()
#file_emps.close()

# #############################################################################################
# Задание №1.  Вывод файла на экран. 
# Допустим, что файл numbers.txt содержит ряд целых чисел и существует на 
# диске компьютера.  Напишите программу, которая выводит на экран все 
# числа в файле.
#print('*'*50)
#num_file = open(r'D:\RPy222\numbers.txt', 'r')
#num = num_file.readline()
#while num != '':
    #print(num)
    #num = num_file.readline()
#num_file.close()
#print('*'*50)
# #############################################################################################
# Задание №2.  Вывод на экран верхней части файла. 
# Напишите программу, которая запрашивает у пользователя имя файла. 
# Программа должна вывести на экран только первые пять строк содержимого файла. 
# Если в файле меньше пяти строк, то она должна вывести на экран все содержимое файла. 
#print('*'*90)
#file_name = input('Введите имя файла: ')
#file_str = open(file_name,'r', encoding='UTF-8')
#line = file_str.readline()
#count = 0
#while line != '':
    #if count < 5:
        #print(line.rstrip('\n'))
        #line = file_str.readline()
        #count += 1
    #else:
        #break
#file_str.close()
#print('*'*90)
# ############################################################################################

# Задание №3.  Номера строк. 
# Напишите программу, которая запрашивает у пользователя имя файла. 
# Программа должна вывести на экран содержимое файла, при этом каждая строка должна 
# предваряться ее номером и двоеточием. Нумерация строк должна начинаться с 1. 
#print('*'*90)
#file_name = input('Введите имя файла: ')
#print('*'*30)
#file_str = open(file_name,'r', encoding='UTF-8')
#line = file_str.readline()
#count = 1
#while line != '':
    #print(f'{count:2}: ' + line.rstrip('\n'))
    #line = file_str.readline()
    #count += 1
#file_str.close()
#print('*'*90)
# #############################################################################################

# Задание №4.  Счетчик значений. 
# Допустим, что файл с серией имен (в виде строковых значений) называется names.txt 
# и существует на диске компьютера. Напишите программу, которая показывает количество 
# хранящихся в файле имен. (Подсказка: откройте файл и прочи­тайте каждую хранящуюся в нем 
# строку.  Примените переменную для подсчета количест­ва прочитанных из файла значений.)
#print('*'*90)
#file_str = open(r'D:\RPy222\data_1.txt','r', encoding='UTF-8')
#line = file_str.readline()
#count = 0
#while line != '':
    #line = file_str.readline()
    #count += 1
#file_str.close()
#print(f'Количество строк в файле {count}.')
#print('*'*90)
# ##############################################################################################

# Задание №5. Сумма чисел. 
# Допустим, что файл с рядом целых чисел называется numbers.txt и суще­ствует на диске 
# компьютера.  Напишите программу, которая  читает все  хранящиеся в файле числа и 
# вычисляет их сумму. 
#print('*'*90)
#file_num = open(r'D:\RPy222\numbers.txt','r', encoding='UTF-8')
#line = file_num.readline()
#total  = 0
#while line != '':
    #num = int(line)
    #total += num
    #line = file_num.readline()
#print(total)
#file_num.close()
#print('*'*90)
# ###############################################################################################

# Задание №6. Среднее арифметическое чисел. 
# Допустим, что файл с рядом целых чис~л называется numbers.txt и существует на диске 
# компьютера. Напишите программу, которая вычисляет среднее арифметическое всех хранящихся 
# в файле чисел.
#print('*'*90)
#file_num = open(r'D:\RPy222\numbers.txt','r', encoding='UTF-8')
#line = file_num.readline()
#total  = 0
#count = 0
#print('Числа последавательности')
#while line != '':
    #num = int(line)
    #total += num
    #line = file_num.readline()
    #count += 1
    #print(f'{num}', end=' ')
#print(f'\nСумма всех чисел = {total}')
#print(f'Среднее арифметическое всех чисел = {total/count:.2f}')
#file_num.close()
#print('*'*90)
# ###############################################################################################
# Задание №7.    
# Программа записи файла со случайными числами. Напишите программу, которая 
# пишет в файл ряд случайных чисел.  Каждое случайное число должно быть в диапазоне 
# от 1 до 500.  Приложение должно предоставлять пользователю возможность назначать 
# количество случайных чисел, которые будут содержаться в файле.
#print('*'*90)
#import random
#numbers = int(input('Введите количество случайных чисел: '))
#file_numbers = open(r'D:\RPy222\numbers_1.txt','w', encoding='UTF-8')
#for num in range(0, numbers):
    #num = random.randint(1, 500)
    #print(num)
    #file_numbers.write(str(num)+'\n')
#file_numbers.close()
#print('*'*90)
# ###############################################################################################

# Задание №7. Программа чтения файлов со случайными числами. 
# Выполнив предыдущее задание (программу записи файла со случайными числами), 
# напишите еще одну программу, кото­рая читает случайные числа из файла, выводит 
# их на экран и затем показывает приведен­ные ниже данные:  
# •  сумму чисел; 
# •  количество случайных чисел, прочитанных из файла.
print('*'*90)
file_num = open(r'D:\RPy222\numbers_1.txt','r', encoding='UTF-8')
total = 0
count = 0
#line = file_num.readline()
#while line != '':
    #num = int(line)
    #print(num, end=' ')
    #total += num
    #count += 1 
    #line = file_num.readline()
for line in file_num:
    num = int(line)
    print(num, end=' ')
    total += num
    count += 1     
print(f'\nСумма чисел = {total}.\nKоличество случайных чисел, прочитанных из файла = {count}.')
file_num.close()
print('*'*90)
# ###############################################################################################

print('END')
