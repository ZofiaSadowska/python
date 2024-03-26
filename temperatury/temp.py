#zadanie 1
import pandas as pd

#zadanie 2

csv = pd.read_csv('temperature.csv', sep=';')
#print(csv.to_string())

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


df.rename(columns={'AverageTemperatureFahr':'AvgTmpF'},inplace=True)
df.rename(columns={'AverageTemperatureUncertaintyFahr':'AvgTmpUnF'},inplace=True)
print(df)

def F2C(tmp):
    return 5*(tmp-32)/9

df['AvgTmpC'] = df['AvgTmpF'].map(F2C)
df['AvgTmpUnC'] = df['AvgTmpUnF'].map(F2C)

del df['AvgTmpUnF']

def Latitude(lat):
    if lat[-1] == 'N':
        return float(lat[:-1])
    elif lat[-1] == 'S':
        return -float(lat[:-1])
    else:
        return 0.0

def Longitude(lon):
    if lon[-1] == 'W':
        return -float(lon[:-1])
    elif lon[-1] == 'E':
        return float(lon[:-1])
    else:
        return 0.0

df['Latitude'] = df['Latitude'].map(Latitude)
df['Longitude'] = df['Longitude'].map(Longitude)
print(df)
