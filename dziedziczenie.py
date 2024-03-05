class figura():
    def __init__(self,*boki) -> None:
        self.boki = boki
        print("Jestem figurą")
        

    def Pole(self):
        print("Nie moge obliczyc pola")
        
    def Obwod(self):
        self.obw = 0
        for i in self.boki:
            self.obw += i
        print(f"Obwod tej figury wynosi: {self.obw}")    

class trojkat(figura):
    def __init__(self,a=0,b=0,c=0,h=0) -> None:
        super().__init__(a,b,c,h)
        self.a = a
        self.b = b
        self.c = c
        self.h = h
        print("Jestem trójkąt")

    def Pole(self):
        print(f"Pole wynosi {self.a*self.h*0.5}") 
        



f1 = figura(1,2,4,2,8,7)
f1.Pole()
f1.Obwod()

f2 = trojkat(3,6,8,3)
f2.Pole()
f2.Obwod()

           

           