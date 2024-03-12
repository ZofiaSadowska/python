import pandas as pd
import random 

lista = []

for el in range (100):
    lista.append(random.randint(0,100))


#slownik = {"styczen": 31, 'luty':28, "marzec":31}
#lista1 = [31,28,31]
#indeksy = ["styczen", "luty", "marzec"]
#krotka = ("uwu", "owo")
dane = pd.Series(lista)
    
#dane2 = pd.Series(lista1)
#dane3 = pd.Series(indeksy)
#dane4 = pd.Series(krotka)

#print(lista)
#print(slownik)
#print(dane4)



#print(dane3.loc[:"marzec"])
#print(dane3.iloc[:3])

dane = pd.Series(lista)
print(dane)
#print(dane.head(10))
print(dane.count())
print (dane.min())
print (dane.max())
print (dane.mean()) #srednia 
print (dane.median()) # wartosc srodkowa
print (dane[dane>50].mean())

print(dane[::2][dane>50].count())


data = { 
    "polish": ['styczen', 'luty', 'marzec', 'kwiecien', 'maj', 'czerwiec', 'lipiec', 'sierpien', 'wrzesien', 'pazdziernik', 'listopad', 'grudzien'],
    "days" : [31,28,31,30,31,30,31,31,30,31,30,31]
}


dataframe = pd.DataFrame(data)
print(dataframe)






