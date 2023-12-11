#!/usr/bin/env python3
# -*- coding: utf-8 -*-

dictionary = {
    2500: 'Строка 1',
    2712: 'Строка 2',
    3450: 'Строка 3',
    2652: 'Строка 4',
    274568: 'Строка 5',
    2454: 'Строка 6',
    2686: 'Строка 7',
    72729: 'Строка 8',
    39872: 'Строка 9'
}

if __name__ == '__main__':
    dict_items = dictionary.items()
    dictionary_reversed = dict((v, k) for k, v in dict_items)

    print("Обновленный словарь school:", dictionary)
    print("Общее количество учащихся в школе:", dictionary_reversed)
