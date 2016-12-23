#!/usr/bin/python

#trzeba uwazac co sie robi, bo gmpy2 zastepuje
#niektore wbudowane funkcje i moga pojawic sie bledy
#tu akurat mi to nie przeszkadza
from gmpy2 import *#zamiast gwiazdki kazda uzyta funkcja

#duze liczby
p=mpz(13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171)
g=mpz(26790476600736210439911326117339978371955050182095051707060863109260114006743503487596200818701323671541681934177621901008556022090467034705794892743945893)
h=mpz(4476678147226155115558365457750475595861521772603596936757528326067178243549776543712192144627870184928567432208656624794079113374237487568153440925199271)

#slownik zlozonosc O(1)
di = {}
y=250000#2**20 w poleceniu bylo, ale 250000 spokojnie wystarczy

#kandydaci na wynik
for i in range(y):
    #https://gmpy2.readthedocs.io/en/latest/mpz.html
    #powmod(x, y, m) returns (x ** y) mod m.
    #f_mod dzielenie mod.
    #mul-mnozenie
    first=powmod(g,i,p)
    second=powmod(first,(-1),p)
    wyn=mul(second,h)
    wynik=f_mod(wyn,p)
    di[wynik]=i

#sprawdzenie po kluczach czy wystepuje
for i in range(len(di)):
    first=powmod(g,y,p)
    second=powmod(first,i,p)
    if di.has_key(second):
        x=di.get(second)#jezeli tak, wez jego wartosc
        break

x=i*y+x
print "x= %s"%x
##########WYNIK########################
#teraz wszystko dziala 'blyskawicznie'
# x wynosi: 54682903145
#######################################



