# -*- coding: utf-8 -*-

import linecache

try:
    text = open('ciph.txt')
    list = []
    list_el = ''
    try:
        for i in range(0,12):
            cipher = linecache.getline('ciph.txt',i)
            list_el = cipher
            list.append(list_el)
        for l in list:
            print l
    finally:

        text.close()

except IOError:
    pass
