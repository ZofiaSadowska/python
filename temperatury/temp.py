#zadanie 1
import pandas as pd

#zadanie 2

csv = pd.read_csv('temperature.csv', sep=';')
print(csv.to_string())

#zadanie 3

df = pd.DataFrame(csv)
print("Ilosc rekordów w obiekcie DF wynosi:", len(df))

#zadanie 4

print(df[:100])
#zadanie 5
print(df[-100:])
#zadanie 6
print(df[['Country', 'City']])
#zadanie 7
print(df[df['Country'] == 'Poland'])
#zadanie 8
print(df[df['City'] == 'Wroclaw'][df['year']>=1900][df['year']<=1999])
#zadanie 9
print(df.loc[df['City'] =='Warsaw'][df['month'] == 1]['AverageTemperatureFahr'].mean())
#zadanie 10
print('Najwyższa: ', df.loc[df['Country']=='Poland']['AverageTemperatureFahr'].max())
print('Najniższa: ', df.loc[df['Country']=='Poland']['AverageTemperatureFahr'].min())