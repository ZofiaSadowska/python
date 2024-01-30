Months= {
  '01':31,
  '02': 28,
  '03' : 31,
  '04' : 30,
  '05' : 31,
  '06': 30,
  '07' : 31,
  '08': 31,
  '09' : 30,
  '10' : 31,
  '11' : 30,
  '12' : 31,
  '21':31,
  '22': 28,
  '23' : 31,
  '24' : 30,
  '25' : 31,
  '26': 30,
  '27' : 31,
  '28': 31,
  '29' : 30,
  '30' : 31,
  '31' : 30,
  '32' : 31,
  '41':31,
  '42': 28,
  '43' : 31,
  '44' : 30,
  '45' : 31,
  '46': 30,
  '47' : 31,
  '48': 31,
  '49' : 30,
  '50' : 31,
  '51' : 30,
  '52' : 31,
  '61':31,
  '62': 28,
  '63' : 31,
  '64' : 30,
  '65' : 31,
  '66': 30,
  '67' : 31,
  '68': 31,
  '69' : 30,
  '70' : 31,
  '71' : 30,
  '72' : 31,
  '81':31,
  '82': 28,
  '83' : 31,
  '84' : 30,
  '85' : 31,
  '86': 30,
  '87' : 31,
  '88': 31,
  '89' : 30,
  '90' : 31,
  '91' : 30,
  '92' : 31,
  

}
pesel = input('pesel: ')

lenght = len(pesel)

numbers = '0123456789'
isNumber = True
for i in pesel:
    if i not in numbers:
      isNumber = False
      print('nie wpisales samych cyfr')
      sys.exit(0)
    

lastNumber = int(pesel[d-1])

sum = int(pesel[0]) + int(pesel[1])*3 + int(pesel[2])*7 + int(pesel[3])*9 + int(pesel[4]) + int(pesel[5])*3 + int(pesel[6])*7 + int(pesel[7])*9 + int(pesel[8]) + int(pesel[9])*3
lenght2 = len(str((sum)))
sum2 = str(sum)
checkSum = int(s[n-1])
checkSum = 10-checkSum

year = pesel[0] + pesel[1]
month = pesel[2] + pesel[3]
if int(year)%4 == 0:
  Months['02']= 29
  Months['22'] = 29
  Months['42'] = 29
  Months['62']= 29
  Months['82'] = 29
day = pesel[4] + pesel[5]




if lenght==11 and checkSum==lastNumber and 1 <= int(day) <= Months[month] and month in Months:

  print("this number pesel is correct")

else:

  print("this number pesel is not correct")

