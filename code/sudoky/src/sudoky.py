#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pprint import pprint
from copy import deepcopy
from time import process_time
from os.path import join, abspath
import sys # для вывода судоку в файле.

# прога, смотрим решена судоку или нет, если да то возвращаем sol
def solve(sudo):
    # можно использовать генератор
    sol = [[y for y in x] for x in sudo]
    if solstep(sol):
        return sol
#прога для решения судоку
def solstep(sol):
    # первый этап-бесконечный цикл, проходим по
    # всем пустым ячейкам и будем подставлять те значения которые
    # однозначны в ячейке
    while True:
        # нужно будет запоминать минимальные значения для ячейки.
        # т.е. в ячейку можно поставить 1 значение значит мин-1, 2 значения
        # мин-2, 3 значения мин - 3 и.т.д.
        min_pos = None
        # перебераем все значения в судоку
        for ri in range(9):
            for ci in range(9):
                # если в ячейку нельзя ничего подставить, т.е. 0,
                # 0 это False, поэтому можно поставить просто : и ничего не писать
                # то пропускаем ее и возвращаемся дальше к циклу. 
                # используем эту конструкцию
                if sol[ri][ci]:
                    continue
                # posible values(какие значения можно подставить)
                pv = gpv(ri, ci, sol)
                # определяем сколько возможных значений значений можно подставить
                pv_count = len(pv)
                # если кол-во цифр, которые можно подставить = 0(типа нет решения)
                if not pv_count:
                    return False
                # если можно подставить только одну цифру, записываем это значени
                if pv_count == 1:
                    # 1 способ. сколько бы цифр не было берется только одна
                    sol[ri][ci], = pv # запятая означает распаковку, т.е. уже значение голое
                # нужно учесть минимальные позиции
                if not min_pos or pv_count < len(min_pos[1]): # len(min_pos[1]) это значение показ. сколько
                                                              # вартантов мы нашли {3, 4, 9}
                    min_pos = (ri, ci), pv  # (R=4 C=4)=[0] {3, 4, 9}=[1]
        #print(min_pos)
        #pr_sudok(sol)
        if not min_pos: #судоку решена
            return True
        # если закончились min_pos[1] = 1 выходим из цикла, дальше ветвления
        elif len(min_pos[1]) >= 2: # если pv = {3, 4, 9} т.е. больше 1-ой цифры
            break
    # Hачало ветвления. организовать ветвление для того чтобы проверять дальше
    # единичное подставление закончилось. Остались варианты только с несколькими вариантами подставления.
    # Для этого надо
    # 1. проанализировать min_pos
    # вытаскиваем значения из min_pos 
    (r, c), z = min_pos # r-row, c-cokumn, z-значение
    for v in z:
        sol_copy = deepcopy(sol)
        # можно использовать генератор
        #sol_copy = [[y for y in x] for x in sol]
        # формируем первое задание, подставляем первео значение из z, z= {.....} и смотрим решается или не решается.
        sol_copy[r][c] = v
        # Если решена судоку возвращаем True, но прежде нужно из sol_copy переписать все значения в (sol)
        if solstep(sol_copy):
            for r in range(9):
                for c in range(9):
                    sol[r][c] = sol_copy[r][c]
            return True
        #return False
        # Если не решена, то возвращаем False. Если решения нет то прога возвращает None, а None и есть False
        # и поэтому return False можно не писать, все будет работать.
        
    

        
# grv - get row values получае значенеи строки. ri - row index
def grv(ri, sudo):
    return set(sudo[ri])

def gcv(ci, sudo):
    return {line[ci] for line in sudo} # используем генератор множеств !!!!!

# програмка для значений в блоке   
def gbv(ri, ci, sudo):
    # выбираем блок для расстановки цифр
    brs = 3*(ri//3) # brs-bloc row start
    bcs = 3*(ci//3) # bcs-bloc column start
    # И через генратор множеств возвращаем блок с цифрами
    return {sudo[brs + x][bcs + y]
            for x in range(3)
            for y in range(3)
            }
# функция для подстановки возможных цифр в блоке(получение возможных чисел в ячейке)
def gpv(ri, ci, sudo):
    res = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    res -= grv(ri, sudo)
    res -= gcv(ci, sudo)
    res -= gbv(ri, ci, sudo)
    return res

# Рисуем сетку судоки, в конце изменим, добавим в аргементы dst, чтобы судоку рисовался в файле
def pr_sudok(s, dst=sys.stdout):
    print('+-------+-------+-------+', file=dst)
    for k in range(9):
        print('|', s[k][0], s[k][1], s[k][2], '|',
                   s[k][3], s[k][4], s[k][5], '|',
                   s[k][6], s[k][7], s[k][8], '|', file=dst)
        if k % 3 == 2:
            print('+-------+-------+-------+', file=dst)

# Алгоритм такой, если число знаем то точно его устанавливаем, если не знаем
# то устанавливаем 0.
sudo1 = [
    [0, 5, 0, 8, 0, 3, 0, 0, 0],
    [0, 8, 3, 6, 2, 0, 0, 0, 0],
    [6, 0, 1, 0, 0, 7, 8, 0, 4],

    [0, 6, 0, 0, 0, 0, 0, 7, 5],
    [5, 0, 9, 1, 0, 6, 3, 0, 8],
    [3, 7, 0, 0, 0, 0, 0, 4, 0],

    [7, 0, 5, 2, 0, 0, 4, 0, 1],
    [0, 0, 0, 0, 1, 8, 5, 6, 0],
    [0, 0, 0, 7, 0, 4, 0, 9, 0],
    ]

sudo = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],

    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],

    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0],
]

def convsud(strsud):
    result = [list(map(int, strsud[i:i+9]))  for i in range(0, 81, 9)]  
    return result
#************************************************************
# сформируем путь к файлу 100 судок.txt в Date
tpath = join('..', 'Data', 'sudoky100.txt')
tpath = abspath(tpath)
print(tpath)

# Нужно записать данные  в файл
spath = join('..', 'Data', 'sudoky_solved.txt')
spath = abspath(spath)
print(spath)

with open(spath, 'wt', encoding='UTF-8') as dst:
    with open(tpath, 'rt', encoding='UTF-8') as src:
        n = 0 # судоку №1. Делаем нумерацию судоку.
        tall0 = process_time()# общее время решения всех судок
        for line in src:
            line = line.strip()
            if len(line) == 81:
                n += 1
                sudolist = convsud(line)
                pr_sudok(sudolist, dst=dst) # dst=dst, это куда надо печатоть
                
                t0 = process_time()
                rez = solve(sudolist)
                t = process_time() - t0 
                
                if rez:
                    pr_sudok(rez, dst=dst)
                    print(f'Судоку {n:3}  решена за {t} секунд.')
                    print(f'Судоку {n:3}  решена за {t} секунд.\n', file=dst)
                else:
                    print(f'Судоку {n:3}  не решена за {t} секунд.')
                    print(f'Судоку {n:3}  не решена за {t} секунд.\n', file=dst)
    tall = process_time() - tall0
    print(f'Все {n} судок решены за {tall} сек.')
    print(f'Все {n} судок решены за {tall} сек.', file=dst)

print('END')
