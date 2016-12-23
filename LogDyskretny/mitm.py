#!/usr/bin/python

#Jako dane wejsciowe... jezeli chodzi o argumenty w lini polecen uzyc sys.argv

from gmpy2 import *

p=mpz(13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171)
g=mpz(26790476600736210439911326117339978371955050182095051707060863109260114006743503487596200818701323671541681934177621901008556022090467034705794892743945893)
h=mpz(4476678147226155115558365457750475595861521772603596936757528326067178243549776543712192144627870184928567432208656624794079113374237487568153440925199271)

li = []
y=2**20

#tworzy liste, szybsze niz xrange -sequence
for x in range(y):
    #https://gmpy2.readthedocs.io/en/latest/mpz.html
    #powmod(x, y, m) returns (x ** y) mod m.
    #f_mod dzielenie mod.
    #mul-mnozenie
    wyn=mul(f_mod(h,p),powmod(g,(-x),p))
    wart=f_mod(wyn,p)
    li.append(wart)

for i in range(len(li)):
    a=i*y
    test = powmod(g,a,p)
    if test in li:
        miejsce=li.index(test)
        break

#Jezu, ale to mieli
x = li[miejsce]
x = i * y + x
print "x = %s" % x
#x = 11515556232004847983596764191775641108997456158658024416768044308569638778892629593675961986565814361059099740944750069747725537322750614729189172123506166
#cos spier...
