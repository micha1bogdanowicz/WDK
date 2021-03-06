#!/usr/bin/python

import Padding
from binascii import unhexlify
from binascii import hexlify
from Crypto.Random import get_random_bytes as magic
from Crypto.Cipher import AES
from Crypto.Util import Counter

class Engine():
    def cls(self):
        print "\n" + "#" * 50 + "\n"

    def WhichAESMethodUse(self):
        print "##################Welcome in CryptoWATer##################"
        print "Write '1' to use Electronic Code Book  ECB (PKCS#5)."
        print "Write '2' to use Cipher-Block Chaining CBC (PKCS#5)."
        print "Write '3' to use CounTeR CTR."
        rodzaj_szyfr = int(raw_input("Which CipherMethod u want to use?  "))
        Engine.cls()
        return rodzaj_szyfr

    def WhichKeyUse(self):
        print "You can load your key to file secret.keyz"
        print "As hex string ofc(after - load last session key)"
        print "New key is always random"
        nowy_klucz = raw_input("Want you to use a last session key('yes'/'no'): ")
        if (nowy_klucz == 'no'):
            secret_key = Engine.CreateSecretKey()
        else:
            secret_key = Engine.ReadKeyFromFile()
            if (secret_key == None):
                print "File not found, create random key"
                secret_key = Engine.CreateSecretKey()
        Engine.cls()
        return unhexlify(secret_key)

    def WhichIvUse(self):
        print "You can load your IV to file secret.iv"
        print "As hex string ofc(after - load last session iv)"
        print "New iv is always random"
        nowy_iv = raw_input("Want you to use a last session iv('yes'/'no'): ")
        if (nowy_iv == 'no'):
            secret_iv = Engine.CreateSecretIV()
        else:
            secret_iv = Engine.ReadIVFromFile()
            if (secret_iv == None):
                print "File not found, create random iv"
                secret_iv = Engine.CreateSecretIV()
        Engine.cls()
        return unhexlify(secret_iv)

    def ReadIVFromFile(self):
        secret_iv = None
        try:
            secret_iv_txt = open('secret.iv')
            secret_iv = secret_iv_txt.read()
        finally:
            secret_iv_txt.close()
            return secret_iv

    def CreateSecretIV(self):
        dlg = 16
        secret_iv = magic(dlg)
        secret_iv = hexlify(secret_iv)
        print "Create %d byte iv: %s \nBackup to file: secret.iv " % (dlg, secret_iv)
        secret_iv_txt = open('secret.iv', 'w')
        secret_iv_txt.write(secret_iv)
        secret_iv_txt.close()
        return secret_iv

    def ReadKeyFromFile(self):
        secret_key = None
        try:
            secret_key_txt = open('secret.keyz')
            secret_key = secret_key_txt.read()
        finally:
            secret_key_txt.close()
            return secret_key

    def CreateSecretKey(self):
        dlg = 16
        secret_key = magic(dlg)
        secret_key = hexlify(secret_key)
        print "Create %d byte key: %s \nBackup to file: secret.keyz " % (dlg, secret_key)
        secret_key_txt = open('secret.keyz', 'w')
        secret_key_txt.write(secret_key)
        secret_key_txt.close()
        return secret_key

    def Encrypt(self,secret_key,mode,iv):
        if (mode == AES.MODE_CTR):
            ctr = Counter.new(128, initial_value=int(hexlify(iv), 16))
            obj = AES.new(secret_key,mode,counter=ctr)
        else:
            obj = AES.new(secret_key,mode,iv)
        text = raw_input("Wprowadz wiadomosc do zaszyfrowania: ")
        if (mode != AES.MODE_CTR):
            text = Padding.appendPadding(text, blocksize=Padding.AES_blocksize, mode='CMS')
        ciph = obj.encrypt(text)
        file = open('cipher.txt','w')
        file.write(hexlify(ciph))
        file.close()
        return ciph

    def Decrypt(self,ciph,secret_key,mode,iv):
        if(mode == AES.MODE_CTR):
            ctr = Counter.new(128, initial_value=int(hexlify(iv), 16))
            obj = AES.new(secret_key, mode, counter=ctr)
        else:
            obj = AES.new(secret_key,mode,iv)
        msg = obj.decrypt(ciph)
        if(mode != AES.MODE_CTR):
            msg = Padding.removePadding(msg, mode='CMS')
        return msg

    def main(self):
        rodzaj = Engine.WhichAESMethodUse()
        EncryptDecrypt = raw_input("You want to encrypt '0' or decrypt  '1' msg? ")
        if (EncryptDecrypt=='0'):
            key = Engine.WhichKeyUse()
            if(rodzaj == 1):
                #ECB nie uzywa iv wiec jego wartosc moze byc domyslna
                ciph=Engine.Encrypt(key,AES.MODE_ECB,iv="0000000000000001")
                msg=Engine.Decrypt(ciph,key,AES.MODE_ECB,iv="0000000000000001")
            if(rodzaj == 2):
                iv = Engine.WhichIvUse()
                ciph=Engine.Encrypt(key,AES.MODE_CBC,iv)
                msg=Engine.Decrypt(ciph,key,AES.MODE_CBC,iv)
            if(rodzaj == 3):
                #Counter generowany na podstawie iv
                iv = Engine.WhichIvUse()
                ciph=Engine.Encrypt(key,AES.MODE_CTR,iv)
                msg = Engine.Decrypt(ciph, key, AES.MODE_CTR, iv)
            print "Twoja zaszyfrowana wiadomosc: " + hexlify(ciph)
            print "Sprawdzenie poprawnosci: " + msg

        if(EncryptDecrypt=='1'):
            print "Load you key to file: 'secret.keyz'"
            print "Load you ciphertext to file: 'cipher.txt'"
            if(rodzaj == 1):
                raw_input("If it done, press 'enter'")
                Engine.cls()
                try:
                    key=unhexlify(Engine.ReadKeyFromFile())
                    filea = open('cipher.txt')
                    ciph =unhexlify(filea.read())
                finally:
                    filea.close()
                    msg = Engine.Decrypt(ciph,key,AES.MODE_ECB,iv="0000000000000001")
            if (rodzaj == 2):
                print "Load you iv to file: 'secret.iv'"
                raw_input("If it done, press 'enter'")
                Engine.cls()
                try:
                    key = unhexlify(Engine.ReadKeyFromFile())
                    filea = open('cipher.txt')
                    ciph = unhexlify(filea.read())
                    iv = unhexlify(Engine.ReadIVFromFile())
                finally:
                    filea.close()
                    msg = Engine.Decrypt(ciph, key, AES.MODE_CBC, iv)
            if (rodzaj == 3):
                print "Load you iv to file: 'secret.iv'"
                raw_input("If it done, press 'enter'")
                Engine.cls()
                try:
                    key = unhexlify(Engine.ReadKeyFromFile())
                    filea = open('cipher.txt')
                    ciph = unhexlify(filea.read())
                    iv=unhexlify(Engine.ReadIVFromFile())
                finally:
                    filea.close()
                    msg = Engine.Decrypt(ciph, key, AES.MODE_CTR, iv)
            print "Decrypt msg: "+msg

if __name__ == "__main__":
    Engine = Engine()
    Engine.main()
