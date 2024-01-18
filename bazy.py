class ksiazki:
    def __init__(self, imieAutora, nazwiskoAutora,  dataWydania, tytul):
        
        self.imie = imieAutora
        self.nazwisko = nazwiskoAutora
        self.data = dataWydania
        self.tytul = tytul

    def __str__(self):
        return self.tytul +' '+ self.nazwisko +' '+ self.imie +' '+ self.data        

def wiersz():
    print("TYTUŁ           AUTOR            DATA")


Id1 = ksiazki('Adam', '     Mickiewicz', '     bog wie kiedy', 'Dziady')
Id2 = ksiazki('Henryk', '      Sienkiewicz', '  nwm', 'Potop')



ksiegarnia = [Id1, Id2]
wiersz()
for el in ksiegarnia:
    {
        print(el)
    }


zapytanie = input("chcesz dodac nowy rekord? jesli tak wpisz 't', jesli nie, 'n'")
if (zapytanie == 't'):
      n =0
      nowy =[]
      while n <4:
        nowy.append(input('podaj wartosc'))
        n+=1
elif zapytanie== 'n':
    print('ok.spierdalaj :-)')
else:
    print('jestes glupi czy jestes glupi?')
    pass


for el in nowy:

    


print (nowy)
        
        
