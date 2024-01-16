class ksiazki:
    def __init__(self, imieAutora, nazwiskoAutora,  dataWydania, tytul):
        
        self.imie = imieAutora
        self.nazwisko = nazwiskoAutora
        self.data = dataWydania
        self.tytul = tytul

    def tekst(self):
        print("ksiazke o tytule", self.tytul)



        
        