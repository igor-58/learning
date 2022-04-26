#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Необходимо написать функцию генератора, реалижующую вычисление факториала и проверить ее работу
с использованием функций list, генератора списков, цикла for и генератора множеств.'''
# Факториал это произведение чисел от 1 до N. n! = 1*2*3*4=24
# Должна выдавать 1, 2, 6, 24, 120,720 и.т.д
# Импортируем Iterator для того чтобы без функции __next__ создание экземпляра класс Fact
# было не возможно. 
from collections.abc import Iterator


class Fact(Iterator):# Базовый абстрактный класс Iterator заменяет класс object
    def __init__(self, nmax=100): # используется как конструктор класса
        if not isinstance(nmax, int):
            raise ValueError('nmax should be int')
        if nmax < 1:
            raise ValueError('nmax should be > 0')
        if nmax > 100:
            raise ValueError('nmax should be <= 100')
        # Запоминаем первое значение для нашей последовательности факториалов
        self.__n = 1 # номер значения факториала 1, 2, 3, 4, и.т.д.
        self.__f = 1 # значение факториала которое уже посчитали 1, 2, 6, 24, 120 и.т.д.
        self.__nmax = nmax # при достижении nmax необходимо остановить итерации
        
    # Метод __next__ будет вызываться при каждой итерации экземпляра класса
    def __next__(self):
        self.__f *= self.__n  # доумножаем предыдущее значение на счетчик
        self.__n += 1         # увеличиваем счетчик на 1
        # при достижении __nmax прекращаем итерации путем выброса исключения StopIteration
        if self.__n > self.__nmax + 1:
            raise StopIteration
        return self.__f # возвращаем очередное значение факториала
    
    # Функция __iter__ необходима чтобы можно было использовать цикл for для итерации
    def __iter__(self):
        return self
    
# Проверка функции генератора с помощью функции next
factor = Fact(12)
print(next(factor))
print(next(factor))
print(next(factor))
print(next(factor))
print(next(factor))
print(next(factor))
print(next(factor))

# подчеркивание это разовая переменная, которая не нужна. Поэтому через zip, функция 
# которая параллельно объяденяет не ограниченное количество последовательностей
# и возвращает список кортежей!!! по минимальной длине кокого нибудь из них.
# В нашем случае подчеркивание и range(20), просто количество 20  факториалов, чтобы исключить бесконечный цикл,
# а num и factor уже высчитывают само значение факториала

# Проверка функции генератора с помощью цикла for
factor3 = Fact(15)
for _, num in zip(range(1,20), factor3): # разбор кортежа
    print(f'for: = {num}')
    
# проверка класса факториал с помощью функции list
factor4 = list(Fact(8))
print(factor4)

# проверка класса факториал с помощью генератора списков
# выведем первые 11 элементов
test = [x for x in Fact(11)]
print(test)

# проверка класса факториал с помощью генератора списков
# выведем первые 11 элементов
for x in Fact(11):
    print(x)
    
# проверка класса факториал с помощью генератора множеств
# выведем первые 9 элементов
test1 = {x for x in Fact(9)}
print(test1)

# Превращение в множество результата работы нашего генератора
test2 = set(Fact(9))
print(test2)


#____________________________________________________________________________________________________#
# from time import process_time # вычислим время выполнения программы
# Сделаем функцию для отладки и подсчета времени выполнения программы
#def factor(n):
    #factorial = 1
    #for mnogitel in range(1, n+1):
        #factorial *= mnogitel
    #return factorial
#x = 10000
#t0 = process_time()
#print(f'x = {x} len(x!) = {len(str(factor(x)))}')
#t = process_time() - t0 
#print(f'Время вычисления программы составило {t} секунд.')


#x = 4000
#t0 = process_time()
#fs = []
#for n in range(1, x):
    #fs.append(len(str(factor(n))))
#t = process_time() - t0 
#print(f'Время вычисления программы создания списка составило {t} секунд.')


print('END')
