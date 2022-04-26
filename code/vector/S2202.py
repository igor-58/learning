#!/usr/bin/env python 3
# -*- coding: utf-8 -*-
from skvek import Vektor

a = Vektor(x=3, y=4)
b = Vektor(x=3, y=-5)
print(a)
print(b)
d = a*b
print(d)
print('*'*50)
print('========   Задание 3.4.2   =========')
a = Vektor(r=6, alfa=0)
b = Vektor(r=5, alfa=120)
print(f'{a =!s}')
print(f'{b =!s}')
print(f'{a*b       =!s}')
print(f'{b*(a-b)   =!s}')
print(f'{a*(a+2*b) =!s}')

print('*'*50)
print('========   Задание 3.4.3   =========')
a = Vektor(r=1, alfa=0)
b = Vektor(r=1, alfa=-30)
c = Vektor(r=1, alfa=30)
print(f'{a =!s}')
print(f'{b =!s}')
print(f'{c =!s}')
print(f'{a*(b+c)         =!s}')
print(f'{(a+c)*(b-c)     =!s}')
print(f'{(2*a-b)*(a+2*b) =!s}')
print(f'{(a+b-c)*(a-b-c) =!s}')

print('*'*50)
print('========   Задание 3.4.4   =========')
x = Vektor(x=2, y=0)
y = Vektor(x=0, y=3)
print(f'{x =!s}')
print(f'{y =!s}')
print(f'{x*(x+y)-y*(x+y) =!s}')
p = Vektor(r=12, alfa=15)
q = Vektor(r=12, alfa=105)
print(f'{p =!s}')
print(f'{q =!s}')
print(f'{(2*p+3*q)*(3*p-2*q) =!s}')
a = Vektor(r=3, alfa=40)
b = Vektor(r=3, alfa=-80)
print(f'{a =!s}')
print(f'{b =!s}')
print(f'{(a+2*b)*(3*a-b) =!s}')

print('*'*50)
print('========   Задание 3.4.5   =========')
a = Vektor(r=5, alfa=0)
b = Vektor(r=8, alfa=60)
print(f'{a =!s}')
print(f'{b =!s}')
print(f'{(a+b).r =!s}')
print(f'{(a-b).r =!s}')


#a.output()
#b.output()
#a.alfa = 45
#a.output() # X = 6.476559, Y = 6.476559, alfa = 45.000000, R = 8.246211
#print(f'{b=}') # b=<skvek.myvek.Vektor object at 0x00000241943C88E0>
# с использованием функции def __repr__
#print(f'{b=}') # b=Vector(x = -3.0000 y = 5.1962 r = 6.0000 alfa = 120.0000)
#print(f'{a.x=}')
#print(f'{a.y=}')
#print(f'{a.r=}')
#print(f'{a.alfa=}')
print('END')
