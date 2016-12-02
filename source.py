# -*- coding: utf-8 -*-
#!/usr/bin/python

import linecache
import binascii
list = []

def xor_strings(bin_a, bin_b):
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(bin_a, bin_b))

def main():
    a=[]
    for element in list:
        x = list[0].decode('hex')
        b = element.decode('hex')
        a.append(xor_strings(x,b))
    a.pop(0)

    crib=raw_input("Crib: ").decode('CP852')
    crib=crib.encode('utf-8')
    for element in a:
        s= xor_strings(element,crib)
        print s.decode('utf-8')

def load_from_file():
    try:
        file = open('ciph.txt','r')
        for line in file:
            list.append(line.rstrip('\n'))
        main()
    finally:
        file.close()


if __name__ == '__main__':
    load_from_file()
    pass
