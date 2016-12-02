# -*- coding: utf-8 -*-
#!/usr/bin/python

import linecache
import binascii
list = []

def xor_strings(bin_a, bin_b):
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(bin_a, bin_b))

def main():
    x = list[1].decode('hex')
    b = list[2].decode('hex')
    a=xor_strings(x,b)
    print a.encode('hex')
    crib=raw_input("Crib: ").decode('CP852')
    crib=crib.encode('utf-8')
    s= xor_strings(a,crib)
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
