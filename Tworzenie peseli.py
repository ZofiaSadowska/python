mport sys
import random


miesiace = {
    '01' : 31,
    '02' : 28,
    '03' : 31,
    '04' : 30,
    '05' : 31,
    '06' : 30,
    '07' : 31,
    '08' : 31,
    '09' : 30,
    '10' : 31,
    '11' : 30,
    '12' : 31
}
stulecia = {
    '18' : 80,
    '19' : 0,
    '20' : 20,
    '21' : 40,
    '22' : 60
}

data = input('wprowadz date urodzenia (rrrrmmdd) ')
plec = input('wprowadz plec K/M ')

if len(data) == 8:
    pass
else:
    print('zle wpisales date (za malo lub za duzo znakow)')
    sys.exit(0)

rrrr = data[0] + data[1] + data[2] + data[3]
if int(rrrr)%4 == 0:
    miesiace['02'] = 29

mm = data[4] + data[5]
dd = data[6] + data [7]

if 1799 < int(rrrr) < 2300 and mm in miesiace and 1 <= int(dd) <= miesiace[mm]:
    pass
else: 
    print("wpisales niepoprawna date, nie jest ona istniejaca datą")
    sys.exit(0)    

if plec.upper() == 'K' or plec.upper() == 'M':
    pass
else: 
    print ('wpisz ponownie oznaczenie plci (k lub m)')    
    sys.exit(0)
pesel = []
pesel.append(rrrr[2])
pesel.append(rrrr[3])
stulecie = rrrr[0] + rrrr[1]

mm = int(stulecia[stulecie]) + int(mm)
mm = str(mm)
if stulecie == '19':
     mm = '0' + mm
pesel.append(mm[0])
pesel.append(mm[1])
pesel.append(dd[0])
pesel.append(dd[1])
zestaw = set()

g = 1
while g <= 5000:
    p = random.randint(0,9)
    p1 = random.randint(0,9)
    p2 = random.randint(0,9)
    if plec.upper() == 'K':
        x = random.randrange(0,10,2)
    else:
        x = random.randrange(1,10,2) 
    pesel.append(str(p))
    pesel.append(str(p1))
    pesel.append(str(p2))
    pesel.append(str(x))
    

    suma = int(pesel[0]) + int(pesel[1])*3 + int(pesel[2])*7 + int(pesel[3])*9 + int(pesel[4]) + int(pesel[5])*3 + int(pesel[6])*7 + int(pesel[7])*9 + int(pesel[8]) + int(pesel[9])*3
    n = len(str(suma))
    s = str(suma)
    suma_k = int(s[n-1])
    suma_k = 10-suma_k
    if suma_k == 10:
         suma_k = 0     

    Pesel = ''
    pesel.append(str(suma_k))
    dPrzed = len(zestaw)
    for ele in pesel:
            Pesel += ele
    zestaw.add(Pesel)
    dPo = len(zestaw)
    if  dPo > dPrzed:
        pesel.pop(10)
        pesel.pop(9)
        pesel.pop(8)
        pesel.pop(7)
        pesel.pop(6)
        g+=1

    else: 
        pesel.pop(10)
        pesel.pop(9)
        pesel.pop(8)
        pesel.pop(7)
        pesel.pop(6)
        pass   


print(zestaw)
print("wszystkie pesele zostaly wypisane")
