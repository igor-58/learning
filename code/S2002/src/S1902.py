#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Формируем путь из этой папки к файлу elochka.txt это для win если прописывать в ручную
# data_path = '..' + '\\' + 'Data' + '\\' + 'elochka.txt'  # ..\Data\elochka.txt
# Есть библиотека которая делает путь для любой операционной системы коректно !!!
from os.path import join, abspath # штатный способ работы с путями. Так и только так !!!

data_path = join('..', 'Data', 'elochka.txt')
print(data_path)                                            #  ..\Data\elochka.txt
data_path = abspath(data_path)  # d:\RPy221\Day19\S1902\Data\elochka.txt
print(data_path)

write_path = join('..', 'Data', 'new_elochka.txt')
print(write_path)
write_path = abspath(write_path)
print(write_path)

# Доступ к файлу рекомендуется писать относительный. Открывать его по абсолютной ссылке.
#src = open(data_path, mode='rt', encoding='utf-8')
# Но через менеджер контекста лучше(гарантирует закрытие файла и выталкивает все из буфера, т.е.
# информация сохраняется.) Только потом идет обработка ошибки.
# Запишем нашу песню в файл
with open(write_path, 'wt', encoding='utf-8') as dst:
    with open(data_path, mode='rt', encoding='utf-8') as src:
        n = 0 #устанавливаем счетчик для подсчета строк, букв и.т.д
        for line in src:
            n += 1
            line = line.strip()
            print(f'{n:3} {len(line):3} {len(line.split()):2} {line}', file = dst)
print('END')
