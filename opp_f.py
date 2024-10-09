from datetime import datetime
import matplotlib.pyplot as plt

def les_data(filnavn,tidskolonen,tempkolonen,file):
 tidspunkter= []
 temperaturer = []
 filnavn='github/oving_6/temperatur_trykk_met_samme_rune_time_datasett.csv.txt'
 startkolone=0
 with open(filnavn, 'r') as fil:
     # Hopper over headeren hvis den finnes
    next(fil)
    for linje in fil:
      linje=linje.strip()
      if not linje:
          continue
      deler=linje.split(';')
      if len(deler) <max(tidskolonen,tempkolonen)+1:
          print('ugildig linje format i denne linjen',linje)
          continue
      if file==2:
          tid=deler[startkolone]+deler[tidskolonen]
          temp=deler[tempkolonen]
      else:  
         tid=deler[tidskolonen]
         temp=deler[tempkolonen]
      if temp==''or temp==' ':
          print('ugildig tempratur',temp)
          continue
      try:
 
       temp=float(temp.replace(',' , '.').strip())
       try:
           tidespunkt=datetime.strptime(tid, '%d.%m.%Y %H:%M')
       except ValueError:
           tidespunkt=datetime.strptime(tid, '%d.%m.%Y %H:%M:%S')
          
       tidspunkter.append(tidespunkt)
       temperaturer.append(temp)
      except ValueError as e:
         print('feil ved konvertering av linjen', linje,'--',e)
         continue
 return tidspunkter,temperaturer
filnavn1='github/oving_6/temperatur_trykk_met_samme_rune_time_datasett.csv.txt'
tidspunkt1,temperatur1=les_data(filnavn1,tidskolonen=2,tempkolonen=3,file=1)
filnavn2='github/oving_6/trykk_og_temperaturlogg_rune_time.csv.txt'
tidspunkt2,temperatur2=les_data(filnavn2,tidskolonen=1,tempkolonen=4,file=2)
print('antall tidspunkter i fil1 er:',len(tidspunkt1))
print('antall temperatureri fil1 er:',len(temperatur1))
print('antall tidspunkter i fil2 er:',len(tidspunkt2))
print('antall temperaturer i fil2 er:',len(temperatur2))
if len(tidspunkt1)==len(temperatur1) and len(tidspunkt2)==len(temperatur2):
 plt.figure(figsize=(10, 5))
    

 plt.figure(figsize=(10,5))
 plt.plot(tidspunkt1,temperatur1, marker='',color='green',label='tempratur',linestyle='-',linewidth=2)
 plt.plot(tidspunkt2,temperatur2, marker='',color='blue',label='tempratur',linestyle='-',linewidth=2)
 plt.xlabel('Tid')
 plt.ylabel('Temperatur (°C)')
 plt.title('Temperatur over tid')
 plt.grid(True)
 plt.xticks(rotation=45)
 plt.tight_layout()
 plt.legend()
 plt.show()
print("Test, test")# Oppgave f

print("Test, test")
