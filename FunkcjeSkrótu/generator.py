#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from Crypto.Hash import MD5, SHA256

for arg in sys.argv[1:]:
    Crypt5 = MD5.new()
    Crypt256 = SHA256.new()

    file = open(arg,'r') #na windowsie dla binarek 'rb' #FOR WINDOWS USER, TO BINARY FILE USE 'rb'
    text = file.read()
    Crypt5.update(text)
    Crypt256.update(text)
    print "Plik: ",arg
    print "Twoja funkcja skrotu(md5): ",Crypt5.hexdigest()
    print "Twoja funkcja skrotu(sha256): ",Crypt256.hexdigest()

    file.close()
