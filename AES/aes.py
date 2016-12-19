#!/usr/bin/python

import Padding
import binascii
from Crypto.Random import get_random_bytes as magic
from Crypto.Cipher import AES

class Engine():
    secret_key = None

    def cls(self):
        print "\n" + "#" * 50 + "\n"

    def CreateSecretKey(self):
        dlg = 16
        secret_key = magic(dlg)
        print "Utworzono %d bajtowy klucz: %s \nWykonano kopie do pliku secret.keyz "%(dlg,binascii.hexlify(secret_key))
        secret_key_txt = open('secret.keyz', 'w')
        secret_key_txt.write(secret_key)
        secret_key_txt.close()
        Engine.cls()
        return secret_key

    def WhichAESMethodUse(self):
        print "##################Welcome in CryptoWATer##################"
        print "Write '0' to use Electronic Code Book  ECB (passwd-based)."
        print "Write '1' to use Cipher-Block Chaining CBC (passwd-based)."
        print "Write '2' to use CounTeR CTR."
        rodzaj_szyfr = int(raw_input("Which CipherMethod u want to use?  "))
        Engine.cls()
        return rodzaj_szyfr

    def EncryptECB(self,secret_key,mode):
        obj = AES.new(secret_key, mode)
        text = raw_input("Wprowadz wiadomosc do zaszyfrowania: ")
        text = Padding.appendPadding(text, blocksize=Padding.AES_blocksize, mode='CMS')
        return obj.encrypt(text)
         #binascii.hexlify(bytearray(ciph))

    def DecryptECB(self,secret_key,ciph):
        obj = AES.new(secret_key,AES.MODE_ECB)
        msg = obj.decrypt(ciph)
        return Padding.removePadding(msg, mode='CMS')

if __name__ == "__main__":
    Engine = Engine()

    cipher_method = Engine.WhichAESMethodUse()
    secret_key = Engine.CreateSecretKey()

    if(cipher_method == 0):
        ciph = Engine.EncryptECB(secret_key,AES.MODE_ECB)
    Engine.cls()
    print binascii.hexlify(ciph)
    Engine.cls()

    ciph = Engine.DecryptECB(secret_key,ciph)
    print ciph