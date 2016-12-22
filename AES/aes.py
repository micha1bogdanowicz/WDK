#!/usr/bin/python
# By tylko rozszyfrowac wiadomosc, podstaw klucz oraz iv do odpowiednich plikow.
# Gdy program spyta sie ktorego klucza/iv uzyc, uzyj tego z ostatniej sesji.
# W Engine.main() w instrukcjach warunkowych IF dodaj '#' na poczatku linijki ciph i pierwszego printa
# dodatkowo dopisz linijke ciph=unhexlify("hexstring")
# przyklad w IF(1)

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
        print "Write '1' to use Electronic Code Book  ECB (passwd-based)."
        print "Write '2' to use Cipher-Block Chaining CBC (passwd-based)."
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
        #Przypadku roszyfrowywania CTR przy bledzie paddingu dodaj '#' w lini ponizej
        msg = Padding.removePadding(msg, mode='CMS')
        return msg

    def main(self):
        rodzaj = Engine.WhichAESMethodUse()
        key = Engine.WhichKeyUse()
        if(rodzaj == 1):
            #ECB nie uzywa iv wiec jego wartosc moze byc domyslna
            # add #ciph = Engine.Encrypt(key, AES.MODE_ECB, iv="0000000000000001")
            # add #print "Twoja zaszyfrowana (ECB) wiadomosc: " + hexlify(ciph)
            # add ciph = unhexlify("mojatajnawiadomosc")
            ciph=Engine.Encrypt(key,AES.MODE_ECB,iv="0000000000000001")
            print "Twoja zaszyfrowana (ECB) wiadomosc: " + hexlify(ciph)
            msg=Engine.Decrypt(ciph,key,AES.MODE_ECB,iv="0000000000000001")
            print "Sprawdzenie poprawnosci: " + msg
        if(rodzaj == 2):
            iv = Engine.WhichIvUse()
            ciph=Engine.Encrypt(key,AES.MODE_CBC,iv)
            print "Twoja zaszyfrowana (CBC) wiadomosc: " + hexlify(ciph)
            msg=Engine.Decrypt(ciph,key,AES.MODE_CBC,iv)
            print "Sprawdzenie poprawnosci: " + msg
        if(rodzaj == 3):
            #Counter generowany na podstawie iv
            iv = Engine.WhichIvUse()
            #ciph=Engine.Encrypt(key,AES.MODE_CTR,iv)
            #print "Twoja zaszyfrowana (CTR) wiadomosc: " + hexlify(ciph)
            ciph = unhexlify("f14379765c8e8433c782e04e1176acabe8a6cde21a7d8b59c62d92d3ea8eefa5594ac43ba123bf9f9bf49196c002c36432794430a77ebdc3fdbe0cf407b7556323ed640b1dfa37460a1de265941b0b8844438b5690cd3b74e8795fe1248339839780cb5b4f0ee3c878e402864c00de050b39a748bf0fbf9e1669fcb2716827523c70fecb1e5d84fa69698e47d28c81c912cc54d962462476ad0a218fc044d469ebee304a5e51490bee8c581da7861ffc18f347d13b28000971837066113815acd529fc9ea74f4d4732288e4ab2a9b51504891461f6e1c752fab2f224bfdec7b377d3f4b3a2d0f507760cfc2c9cc4d6019fb7086837297480405b79f954637ccfb6daa4")
            msg = Engine.Decrypt(ciph, key, AES.MODE_CTR, iv)
            print "Sprawdzenie poprawnosci: " + msg

if __name__ == "__main__":
    Engine = Engine()
    Engine.main()
