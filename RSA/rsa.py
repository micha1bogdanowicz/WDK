#!/usr/bin/python

#Wzorujac sie na https://www.dlitz.net/software/pycrypto/doc/#crypto-publickey-public-key-algorithms
from Crypto.PublicKey import RSA
from Crypto import Random

print "If it your first run, generate key(you can change generate files)"
if(raw_input("Do you want to generate key? '0' - no '1' yes : ")=='1'):
    #Generowanie klucza
    randomgen = Random.new().read
    key = RSA.generate(4096, randomgen)

    private_handler = open("privateKeyFile.pem", 'w')
    private_handler.write(key.exportKey(format='PEM'))
    private_handler.close()

    public_handler = open("publicKeyFile.pem", 'w')
    public_handler.write(key.publickey().exportKey(format='PEM'))
    public_handler.close()

#Szyfrowanie
print "If you want using your key in encrypted - add it to file publicKeyFile.pem"
if(raw_input("Do you want to encrypt file? '0' - no '1' - yes :")=='1'):
    public_handler = open('publicKeyFile.pem', 'r')
    file_name = raw_input("Enter name of file to encrypt")
    file_to_encrypt= open(file_name,'r')
    file_encrypted = open('cipher.txt','w')
    public_key = RSA.importKey(public_handler.read())
    msg = file_to_encrypt.read()
    cipher = public_key.encrypt(msg, 32)
    file_encrypted.write(cipher[0].encode('hex'))

    file_to_encrypt.close()
    file_encrypted.close()
    public_handler.close()


#Deszyfrowanie
print "Import your private key to file privateKeyFile.pem"
if(raw_input("Do you want to decrypt file(hex)? '0' - no '1' - yes :")=='1'):
    private_handler = open('privateKeyFile.pem', 'r')
    file_name = raw_input("Enter name of file to decrypt")
    file_to_decrypt = open(file_name, 'r')
    file_decrypted = open('plaintext.txt', 'w')
    private_key = RSA.importKey(private_handler.read())
    cipher = (file_to_decrypt.read()).decode('hex')
    msg = private_key.decrypt(cipher)
    file_decrypted.write(msg)

    file_to_decrypt.close()
    file_decrypted.close()
    private_handler.close()

