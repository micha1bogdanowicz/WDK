# -*- coding: utf-8 -*-
#!/usr/bin/python

import linecache
import binascii
list = []

def xor_strings(bin_a, bin_b):
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(bin_a, bin_b))

def main():
    a=[]
    crib_ciph=raw_input("W ktorym ciagu znajduje sie szukana fraza? (0-11) ")
    crib_ciph =  int(crib_ciph)
    for element in list:
        x = list[crib_ciph].decode('hex')
        b = element.decode('hex')
        a.append(xor_strings(x,b))
    #a.pop(0)

    crib=raw_input("Crib: ").decode('CP852')
    crib=crib.encode('utf-8')
    i=0
    for element in a:
        if(len(crib)<len(element)):
            s= xor_strings(element,crib)
            print str(i).encode("utf-8")+' '+ s.decode('utf-8','ignore')
        else:
            try:
                s = xor_strings(element, crib)
                print str(i) +' '+ s.decode('utf-8','ignore') + ' ####'

            finally:
                "####KONIEC CIPHER_TXT####"
        i = i + 1



def load_from_file():
    try:
        file = open('ciph.txt','r')
        for line in file:
            list.append(line.rstrip('\n'))
        ext=' '
        while(ext!='exit()'):
            main()
            ext = raw_input("'exit()' - to close, anything to continue: ")
    finally:
        file.close()


if __name__ == '__main__':
    load_from_file()
    pass
