#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   Задачи по программированию  

# Задание №1.  Конвертер километров.
# Напишите программу, которая просит пользователя ввести рас­стояние в километрах 
# и затем это расстояние преобразует в мили. Формула преобразова­ния: 
# мили = километры х 0.6214. 
#print('*'*60)
#rasst = int(input('Введите расстояние в километрах: '))
#def change_km(r):
    #return r * 0.6214
#print(f'Расстояние в {rasst} км = {change_km(rasst):.2f} миль.')
#print('*'*60)

#**********************************************************************************
# Задание №2. Модернизация программы расчета налога с продаж.
# Программа расчета налога с продаж. Требовалось написать программу, которая вычисляет и 
# показывает региональный и федеральный налоги с про­даж, взимаемые при покупке. 
# если эта программа уже вами написана, модернизируйте ее так, чтобы подзадачи были 
# помещены в функции. Если вы ее еще не написали, то напи­шите с использованием функций.
#print('*'*60)
#FED_RATE = 0.05
#REGION_RATE = 0.025
#def region_nalog(purchase):
    #return purchase * REGION_RATE
#def federal_nalog(purchase):
    #return purchase * FED_RATE
#def obchi_nalog(rn, fn):
    #return rn + fn
#def total_purchase(o, p):
    #return o + p
#def print_information(sum_purchase, f, r, o, all_purchase):
    #print(f'Сумма покупки составляет {sum_purchase:.2f} рублей.')
    #print(f'Федеральный налог с продаж составляет {f:.2f} рублей.')
    #print(f'Региональный налог с продаж составляет {r:.2f} рублей.')
    #print(f'Общий налог с продаж составляет {o:.2f} рублей.')
    #print(f'Общая сумма покупки составляет {all_purchase:.2f} рублей.')    
    
#def main():
    #purchase_amount = float(input('Введите сумму покупки: ')) 
    #fn = federal_nalog(purchase_amount)
    #rn = region_nalog(purchase_amount)
    #on = fn + rn
    #rez = on + purchase_amount
    #print_information(purchase_amount, fn, rn, on, rez)
#main()
#print('*'*60)

# ***********************************************************************************************
# Задание №3.  Какова стоимость страховки?
# Многие финансовые эксперты рекомендуют собственни­кам недвижимого имущества 
# страховать свои дома или здания как минимум на 80% сум­мы замещения строения.  
# Напишите программу, которая  просит пользователя  ввести стоимость строения и затем 
# показывает минимальную страховую сумму, на которую он должен застраховать недвижимое имущество.
#print('*'*60)
#def min_strax(summ):
    #return summ*0.8
#summa = float(input('Введите стоимость строения: '))
#min_summ = min_strax(summa)
#print(f'Минимальная страховую сумма, на которую нужно застраховать \
#недвижимое имущество {min_summ:.2f} рублей.')
#print('*'*60)

#*************************************************************************************************
# Задание №4.  Расходы на автомобиль. 
#Напишите программу, которая просит пользователя ввести месячные расходы на следующие 
#нужды, связанные с его автомобилем: 
#платеж по креди­ту,  
#страховка,  
#бензин,  
#машинное масло,  
#шины и 
#техобслуживание. 
#Затем программа должна показать общую месячную стоимость и 
#общую годовую стоимость этих расходов. 
#print('*'*60)
#def pay_to_month(pc, ps, pb, po, pk, pt):
    #return pc + ps + pb + po + pk + pt
#def pay_to_year(summ):
    #return summ * 12
#pay_to_credit = float(input('Введите ежемесячный платеж по кредиту: '))
#pay_straxovra = float(input('Введите ежемесячный платеж по страховке: '))
#pay_to_benzin = float(input('Введите ежемесячный расход на бензин: '))
#pay_to_oil = float(input('Введите ежемесячный расход на машинное масло: '))
#pay_to_kolesa = float(input('Введите ежемесячный расход шины: '))
#pay_to_texno = float(input('Введите ежемесячный расход техобслуживание: '))     
#rez_1 = pay_to_month(pay_to_credit, pay_straxovra, pay_to_benzin, pay_to_oil, pay_to_kolesa,\
                    #pay_to_texno)
#rez_2 = pay_to_year(rez_1)
#print(f'Ежемесячный расход: {rez_1} рублей.')
#print(f'Годовой расход: {rez_2} рублей.')
#print('*'*60)

#*************************************************************************************************
# Задание №5. Налог на недвижимое имущество. 
# Муниципальный округ собирает налоги на недвижи­мое имущество на основе оценочной 
# стоимости имущества, составляющей 60% его фак­тической стоимости. 
# Например, если акр земли оценен в 1О ООО долларов, то его оценоч­ная стоимость 
# составит 6000  долларов.  В этом случае налог на имущество составит 
# 72 цента  за  каждые  100  долларов  оценочной  стоимости.  Налог на  акр,  оцененный 
# в 6000 долларов, составит 43,20  доллара.  Напишите программу, которая запрашивает 
# фактическую стоимость недвижимого имущества и показывает оценочную стоимость и 
# налог на имущество.
#print('*'*60)
#def ocen_stoimost(summ):
    #return summ * 0.6
#def nalog_imychestvo(summ):
    #return (ocen_stoimost(summ)*0.72)/100
#fact_purchase = float(input('Введите фактическую стоимость недвижимого имущества: '))
#print(f'Оценочную стоимость составляет: {ocen_stoimost(fact_purchase):.2f} долларов.')
#print(f'Налог на имущество составляет: {nalog_imychestvo(fact_purchase):.2f} долларов.')
#print('*'*60)
#*************************************************************************************************
# Задание №6.  Калории за счет жиров и углеводов.
#Диетолог работает в спортивном клубе и дает рекомендации клиентам в отношении диеты. 
#В рамках своих рекомендаций он запраши­вает у клиентов количество граммов жиров и 
#углеводов, которые они употребили за день. 
#Затем на основе приведенной ниже формулы он вычисляет количество калорий, которые 
#получаются в результате употребления жиров: 
#калории от жиров =  граммы жиров х 9. 
#Затем на основе еще одной формулы он вычисляет количество калорий, которые получа­
#ются в результате употребления углеводов: 
#калории от углеводов =  граммы углеводов х 4. 
#Диетолог просит вас написать программу, которая выполнит эти расчеты. 
#print('*'*60)
#def get_zir():
    #zir = int(input('Введите количество граммов жиров за день: '))
    #return zir
#def get_yglevody():
    #ygl = int(input('Введите количество граммов углеводов за день: '))
    #return ygl
#def kol_zir(kol):
    #rez = kol*9
    #return rez
#def kol_yg(kol):
    #rez = kol*4
    #return rez
#zir = get_zir()
#ygl = get_yglevody()
#kolor_zir = kol_zir(zir)
#kolor_ygl = kol_yg(ygl)
#print(f'Количество калорий, в результате употребления жиров: {kolor_zir:.2f}')
#print(f'Количество калорий, в результате употребления углеводов: {kolor_ygl:.2f}')
#print('*'*60)
#************************************************************************************************
# Задание №7. Сидячие места на стадионе.
# На стадионе имеется три категории сидячих мест. Места класса А стоят 20 долларов, 
# места класса В  15  долларов и места класса С  10 долла­ров. 
# Напишите программу, которая запрашивает, сколько билетов каждого класса было 
# продано, и затем выводит сумму дохода, полученного за счет продажи билетов.
#***********************************************************************************************
# Задание №13. Максимальное из двух значений.
# Напишите функцию max,  которая в качестве аргу­ментов принимает два целочисленных 
# значения и возвращает значение, которое являет­ся большим из двух. 
# Например, если в качестве аргументов переданы 7 и 12, то функция 
# должна вернуть 12.  Примените функцию в программе, которая предлагает пользователю 
# ввести два целочисленных значения. Программа должна показать большее значение из двух. 
#print('*'*60)
#def maxi(n1, n2):
    #if n1 > n2:
        #return n1
    #else:
        #return n2
#num1 = int(input('Введите первое число: '))
#num2 = int(input('Введите второе число: '))
#rez = maxi(num1, num2)
#print(rez)
#print('*'*60)
#***********************************************************************************************
# Задание №14.  Высота падения.
# При падении тела под действием силы тяжести для определения рас­стояния, которое 
# тело пролетит за определенное время, применяется формула: 
# d = 1/2gt2, 
# где d- расстояние, м; g =  9.8, м/с2;  t- время падения тела, с. 
# Напишите функцию falling  dtstance, которая в качестве аргумента принимает время 
# падения тела (в секундах). Функция должна вернуть расстояние в метрах, которое тело 
# пролетело во время этого промежутка времени. Напишите программу, которая вызывает 
# эту функцию в цикле, передает значения от 1 до 10 в качестве аргументов и показывает 
# возвращаемое значение. 
#print('*'*45)
#def falling_dtstance(time):
    #d = (1/2)*9.8*(time**2)
    #return d
#for i in range(1, 11):
    #n = falling_dtstance(i)
    #print(f'За {i:2} секунд, тело пролетело {n:8.1f} метров.')
#print('*'*45)
#***********************************************************************************************************
# Задание №15.  Кинетическая энергия. 
# Из физики известно, что движущееся тело имеет кинетическую энергию. Приведенная ниже формула 
# может использоваться для определения кинетиче­ской энергии движущегося тела: 
# КЕ =  1/2mv2, 
# где КЕ - это кинетическая энергия; т - масса тела, кг; v - скорость тела, м/с. 
# Напишите функцию kinetic energy,  которая в качестве аргументов принимает массу 
# тела (в килограммах) и его скорость (в метрах в секунду). Данная функция должна 
# вернуть величину кинетической энергии этого тела. Напишите программу, которая про­
# сит  пользователя  ввести  значения  массы  и  скорости,  а  затем  вызывает  функцию 
# kinetic_energy, чтобы получить кинетическую энергию тела.
#print('*'*90)
#def kinetic_energy(massa, speed):
    #ke = 0.5*massa*speed**2
    #return ke
#m = float(input('Введите значение массы тела килограммах: '))
#s = float(input('Введите значение скорости тела в метрах в секунду: '))
#kin_en = kinetic_energy(m, s)
#print(f'При скорости {s} м/с и массе тела {m} киллограм, кинетическая энергия = {kin_en} Дж.')
#print('*'*90)
#********************************************************************************************************
# Задание №16. Средний балл и его уровень.
# Напишите программу, которая просит пользователя вве­сти  пять экзаменационных оценок.  
# Программа должна показать буквенный уровень оценки для каждой оценки и средний балл. 
# Напишите в программе приведенные ниже функции: 
# •  calc  average - функция должна принимать в качестве аргументов пять оценок и 
                   #возвращать средний балл; 
# •  determine  grade - функция должна принимать в качестве аргумента оценку и воз­вращать
                      #буквенный уровень оценки.
#print('*'*90)
#num_1 = int(input('Введите первую оценку: '))
#num_2 = int(input('Введите вторую оценку: '))
#num_3 = int(input('Введите третью оценку: '))
#num_4 = int(input('Введите четвертую оценку: '))
#num_5 = int(input('Введите пятую оценку: '))
#def calc_average(n1, n2, n3, n4, n5):
    #return (n1 + n2 + n3 + n4 + n5)/5
#def determine_grade(num):
    #if num >= 90:
        #num = 'A'
    #elif num <= 89 and num >= 80:
        #num = 'B'
    #elif num <= 79 and num >= 70:
        #num = 'C'
    #elif num <= 69 and num >= 60:
        #num = 'D'
    #elif num < 60:
        #num = 'F'
    #return num
#print('*'*90)
#average_mark = calc_average(num_1, num_2, num_3, num_4, num_5)
#print(f'Ваш средний балл = {average_mark}')
#print('*'*90)
#for i in (num_1, num_2, num_3, num_4, num_5):
    #print(f'Для оценки {i:4} буквенный уровень => "{determine_grade(i)}"')
#print('*'*90)
#*********************************************************************************************************
# Задание №17.  Счетчик четных/нечетных чисел. 
# В этой главе вы увидели пример написания алго­ритма, который определяет четность или нечетность числа. 
# Напишите программу, кото­рая генерирует 100  случайных чисел и подсчитывает количество четных и нечетных 
# случайных чисел. 
#import random
#print('*'*90)
#ch = 0
#nech = 0
#for _ in range(1, 101):
    #num = random.randrange(1, 101)
    #print(num, end=' ')
    #if num % 2 == 0:
        #ch += 1
    #elif num % 2 != 0:
        #nech += 1
#print(f'\nВ этой последовательности {ch} четных и {nech} нечетных чисел.')   
#print('*'*90)
#****************************************************************************************************************

# Задание №18.   Простые числа. 
# Простое число - это число, которое делится без остатка на само себя и 1.  
# Например, число 5  является простым, потому что оно делится без остатка только 
# на 1 и 5.  Однако число 6 не является простым, потому что оно делится без остатка на 1, 2,  3 и 6. 
# Напишите булеву функцию is_prime,  которая в качестве аргумента принимает целое 
# число и возвращает истину, если аргумент является простым числом, либо ложь в про­тивном случае.
# Примените функцию в программе, которая предлагает пользователю вве­сти число и затем выводит 
# сообщение с указанием, является ли это число простым. 
#print('*'*90)
#def is_prime(namber):
    #k = 0
    #for i in range(2, namber // 2+1):
        #if (namber % i == 0):
            #k = k+1
    #if (k <= 0):
        #status = True
    #else:
        #status = False
    #return status
    
#def is_prime(namber):
    #k = 0
    #for i in range(1, namber+1):
        #if (namber % i == 0):
            #k = k+1
    #if (k == 2):
        #status = True
    #else:
        #status = False
    #return status
#num = int(input('Введите число: '))
#if is_prime(num):
    #print('Это простое число.')
#else:
    #print('Это не простое число.')
#print('*'*90)
#*****************************************************************************************************************

# Задание №19.  Список простых чисел. 
#Это упражнение предполагает, что вы уже написали функцию 
#is _pr ime в задаче 18.  Напишите еще одну программу, которая показывает все простые 
#числа от 1до100. Программа должна иметь цикл, который вызывает функцию is prime. 
#print('*'*90)
#spis = []
#def is_prime(namber):
    #k = 0
    #for i in range(1, 102):
        #if (namber % i == 0):
            #k = k+1
    #if (k == 2):
        #status = True
    #else:
        #status = False
    #return status
#for i in range(1, 102):
    #res = is_prime(i)
    #if res == True:
        #spis.append(i)
#print(spis)
#print('*'*90)
#******************************************************************************************************

# Задание №20.   Будущая стоимость. 
#Предположим, что на вашем сберегательном счете есть опреде­ленная сумма денег, и счет 
#приносит составной ежемесячный процентный доход. Вы хо­тите вычислить сумму, которую 
#будете иметь после определенного количества месяцев. 
#Формула приведена ниже: 
#F =  Р х ( 1 + i)2, 
#где F - будущая сумма на счете после указанного периода времени; Р - текущая сум­ма на счете; 
#i - ежемесячная процентная ставка; t - количество месяцев. 
#Напишите программу, которая предлагает пользователю ввести текущую сумму на сче­те, ежемесячную
#процентную ставку и количество месяцев, в течение которых деньги 
#будут находиться на счете. Программа должна передать эти значения в функцию, кото­рая возвращает
#будущую сумму на счете после заданного количества месяцев. Програм­ма должна показать будущую сумму на счете. 
#print('*'*90)
#curent_summ = int(input('Введите текущую сумму на счете: '))
#procent = int(input('Введите ежемесячную процентную ставку: '))
#kol_mouns = int(input('Введите количество месяцев: '))
#def futher_summ( cs, pr, km):
    #pr = pr/100
    #return cs*(km + pr)**2
#print(f'Будующая сумма на счете {futher_summ(curent_summ,procent,kol_mouns):.2f}.')
#print('*'*90)
#*****************************************************************************************************************
# Задание №21.  Игра в угадывание случайного числа.
# Напишите программу, которая генерирует слу­чайное число в диапазоне от 1 до 100 и просит 
# пользователя угадать это число. Если до­гадка пользователя больше случайного числа, 
# то программа должна вывести сообщение 
# "Слишком много, попробуйте еще раз". Если догадка меньше случайного числа, то про­
# грамма должна вывести сообщение "Слишком мало, попробуйте еще раз". Если пользо­ватель число угадывает, 
# то приложение должно поздравить пользователя и сгенериро­вать новое случайное число, чтобы возобновить игру. 
# Необязательное улучшение: улучшите игру, чтобы она вела подсчет догадок, которые 
# делает пользователь. Когда пользователь угадывает случайное число правильно, про­грамма должна показать 
# количество догадок.
#print('*'*90)
#import random
#print('\tИгра угадай чило')
#print('-'*30)
#passw = 'y'
#num = random.randint(1,101)
#print(num)
#count = 0
#while passw == 'y':
    #count += 1
    #number = int(input('Введите число : '))
    #if number < num:
        #print('"Слишком мало попробуйте еще раз".')
    #elif number > num:
        #print('"Слишком много попробуйте еще раз".')
    #else:
        #print(f'Поздравляем вы угадали число {num} за {count} попыток.')
        #num = random.randint(1,101)
        #print(num)
        #passw = input('Хотите сыграть еще? нажмите "y": ')
        #count = 0
#print('*'*90)
#************************************************************************************************************
# Задание №22.  Игра "Камень, ножницы, бумага". 
#Напишите программу, которая дает пользователю возможность поиграть с компьютером в игру
#"Камень, ножницы, бумага". Программа должна работать следующим образом: 
#1.  Когда программа запускается, генерируется случайное число в диапазоне от 1 до 3. 
    #Если число равняется 1,  то компьютер выбрал камень. Если число равняется 2,  то 
    #компьютер выбрал ножницы. Если число равняется 3, то компьютер выбрал бумагу. 
    #(Пока не показывайте выбор компьютера.) 
#2.  Пользователь вводит на клавиатуре выбранный вариант "камень", "ножницы" или "бумага". 
#3.  Выбор компьютера выводится на экран. 
#4.  Победитель выбирается согласно следующим правилам: 
    #-  если один игрок выбирает камень, а другой игрок выбирает ножницы, то побежда­ет 
       #камень (камень разбивает ножницы); 
    #-  если один игрок выбирает ножницы, а другой игрок выбирает бумагу, то побеж­дают
       #ножницы (ножницы режут бумагу); 
    #-  если один игрок выбирает бумагу, а другой игрок выбирает камень, то побеждает 
       #бумага (бумага заворачивает камень); 
    #-  если оба игрока делают одинаковый выбор, то для определения победителя нужно 
       #сыграть повторный раунд. 
import random
print('*'*90)
print('\tИгра "Камень, ножницы, бумага". ')
print('-'*50)
STOUN = 'Камень'
NOZN = 'Ножницы'
PEIPER = 'Бумага'
passw = 'y'
num = random.randint(1, 3)
def menu():
    print('   МЕНЮ')
    print('_'*12)
    print('1 - Камень')
    print('2 - Ножницы')
    print('3 - Бумага')
    print('_'*12)
def get_comp(number):
    if number == 1:
        rez = 'Камень'
    elif number == 2:
        rez = 'Ножницы'
    elif number == 3:
        rez = 'Бумага'
    return rez
def get_igrok():
    number = int(input('Выберите один из пунктов меню '))
    if number == 1:
        rez = STOUN
    elif number == 2:
        rez = NOZN
    elif number == 3:
        rez = PEIPER
    return rez
while passw == 'y':
    def get_result(user_1, user_2):
        if user_1 == 'Камень' and user_2 == 'Ножницы':
            print(f'Победу одержал {user_1}.')
        elif user_1 == 'Ножницы' and user_2 == 'Камень':
            print(f'Победу одержал {user_2}.')
        elif user_1 == 'Ножницы' and user_2 == 'Бумага':
            print(f'Победу одержал {user_1}.')
        elif user_1 == 'Бумага' and user_2 == 'Ножницы':
            print(f'Победу одержал {user_2}.')
        elif user_1 == 'Бумага' and user_2 == 'Камень':
            print(f'Победу одержал {user_1}.')
        elif user_1 == 'Камень' and user_2 == 'Бумага':
            print(f'Победу одержал {user_2}.')    
        elif user_1 == user_2:
            print(f'Ничья.')              
    menu()
    user_1 = get_igrok()
    user_2 = get_comp(num)
    print(f'Компьютер выбрал {user_2}')
    print(f'Вы выбрали {user_1}')
    get_result(user_1, user_2)
    passw = input('Хотите сыграть еще? Набирите "y" если да: ')
#********************************************************************************************************************
print('END')
