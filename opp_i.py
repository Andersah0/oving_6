import matplotlib.pyplot as plt

#funksjon for å lese datene fra den første fil
def les_data_fil1(filnavn):
    datoer=[]
    barometer_trykk=[]
    with open(filnavn,'r') as fil:
        for linje in fil:
            if linje=='Dato' or linje=='Trykk':
                continue
            
            deler=linje.strip().split(';')
            if len(deler)<3 or deler[2]==''or deler[0]=='':
                print('ugildy verdi i linjen ', linje)
                continue
            try:
                 datoer.append(deler[0]+' '+deler[1])
                 barometer_trykk.append(float(deler[2].replace(',','.')))
                 if len(datoer)==3373:
                    barometer_trykk.append(101.220)  
            except ValueError:
                  print('ugildig verdi i linjen', linje)
                  continue
     
    return datoer, barometer_trykk
#funksjon for å les andre fil:

def les_data_fil2(filnavn):
    datoer=[]
    atmosfærisk_trykk=[]
    with open(filnavn,'r') as fil:
        for linje in fil:
            if linje=='Navn' or linje=='Tid':
                continue
       
            deler=linje.strip().split(';')
            if len(deler)<5 or deler[4]==''or deler[4]==' ':
                print('ugildy verdi i linjen ', linje)
                continue
            try:
              datoer.append(deler[2])
              atmosfærisk_trykk.append(float(deler[4].replace(',','.')))
            except ValueError:
                    print('ugildig verdi i linjen', linje)
                    continue
    return datoer, atmosfærisk_trykk    

datoer1, barometer_trykk1=les_data_fil1('github/oving_6/trykk_og_temperaturlogg_rune_time.csv.txt')
datoer2, atmosfæriskk_trykk2=les_data_fil1('github/oving_6/temperatur_trykk_met_samme_rune_time_datasett.csv.txt')
print('det er datoer i første fil:',len(datoer1))
print('det er barometre i første fil',len(barometer_trykk1))
print('det er datoer i andre fil:',len(datoer2))
print('det er atmosfærisk trykk',len(atmosfæriskk_trykk2))
#plotting:
plt.figure(figsize=(10,5))
plt.plot(datoer1,barometer_trykk1,label='barometrisk trykk',color='blue')
#plt.plot(datoer2,atmosfæriskk_trykk2,label='atmosfærisk trykk',color='blue',linestyle='--')
plt.xlabel('tid')
plt.ylabel('Trykk')
plt.xticks(rotasion=45)
plt.legend()
plt.tight_layout()
plt.show()

    # Oppgave i
