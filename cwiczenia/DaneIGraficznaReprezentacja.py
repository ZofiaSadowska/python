import pandas as pd
from matplotlib import pyplot

players = pd.read_csv('players-data.csv', sep=';')
collages = pd.read_csv('players-collage.csv', sep=';')
salaries = pd.read_csv('players-salary.csv', sep=';')

print(players.head(3))
print(players.info())
print(collages.head(3))
print(collages.info())
print(salaries.head(3))
print(salaries.info())

wynik1 = pd.merge(left = players, right=collages, how= 'inner')
merged_inner = wynik1.merge(salaries,how= 'inner')

print(merged_inner)
print(merged_inner.info())
print(len(merged_inner))

wynik2 = players.merge(right=collages, how= 'left')
merged_left = wynik2.merge(right=salaries,how='left')


print(merged_left)
print(merged_left.info())
print(len(merged_left))

#zrobc bez def
def x(w:float) -> float:        #ibs na kg
    return float(w*0.45359237)

def y(w:str) ->float:           #stopy na cm
    d = w.split("-")
    return float(d[0])*30.48 + d([1])*2.54


merged_left['Height'] = merged_left['Height'].map(y)
merged_left['Weight'] = merged_left['Weight'].map(x)


grp1 = merged_left.groupby('Team').agg(srednie = ('Salary', 'mean'))

grp1['srednie'] = grp1['srednie'].map('{:,.2f} $'.format)
