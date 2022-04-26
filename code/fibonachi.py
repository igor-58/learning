#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fib(n):
    fib1 = fib2 = 1 
    #n = int(input('Введите максимальное число Фибоначи: ')) 
    print(fib1, fib2, end=' ')
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
#         print(fib2, end=' ')
        return fib2

# test = list(fib(20))
# print(test)

test = [x for x in fib(20)]
print(test)
