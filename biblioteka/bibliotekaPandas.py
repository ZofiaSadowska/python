import pandas as pd
#import random as rnd



csv = pd.read_csv("Pracownicy 2.csv")

print(csv)
df = pd.DataFrame(csv)
#print(df[["Imię", "Nazwisko"]].to_string())

print(df[df["Płeć"]== "F"].to_string())
print(df[df['Nazwisko']=="Duda"].to_string())


PLN = []
for el in df['Zarobki']:
    PLN.append(float((el[:-4]).replace(' ','')))

df['PLN'] = PLN
del df['Zarobki']
print(df[df['PLN']>5000])

zb = []
for el in df['Płeć']:
    if(df[df['Płeć'] == "F"]):
        zb.append((df[df["Zarobki"]]))









# dane = {
#     "d": [rnd.randint(0,100) for _ in range(0,10)],
#     "e" : ["1","2","3","4","5","6","7","8","9","10"]
# }

# df = pd.DataFrame(dane)

# #dane = [92, 22, 75, 45, 41, 79, 36, 73, 60, 40, 3, 66, 8, 58, 59, 61, 43, 17, 74, 70, 85, 13, 24, 8, 90, 70, 36, 86, 31, 10, 1, 10, 36, 84, 
# #32, 96, 97, 87, 85, 64, 1, 50, 35, 44, 21, 78, 17, 100, 19, 85, 69, 23, 87, 5, 75, 81, 47, 11, 57, 5, 53, 49, 74, 7, 74, 29, 4, 57, 96, 38, 62, 95, 70, 50, 69, 19, 18, 44, 1, 74, 35, 22, 63, 66, 20, 88, 5, 53, 100, 42, 80, 92, 1, 32, 83, 16, 37, 38, 20, 43]

# dane = [rnd.randint(0,100) for _ in range(0,10)]
# print(dane)

# sr = pd.Series(dane)
# print(sr)
# print(sr.loc[2])
# print(sr.iloc[2])


