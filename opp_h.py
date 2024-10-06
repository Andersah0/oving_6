# Oppgave h

import matplotlib.pyplot as plt
import pandas as pd

# Importerer filen temperatur_trykk_met_samme_rune_time_datasett.csv.txt fra oppgave e
from  opp_e import les_fil1, les_fil2 # type: ignore

# Leser filen
df1 = les_fil1('temperatur_trykk_met_samme_rune_time_datasett.csv.txt')

# Finner verdiene og tidene vi vil ha. Fra kl. 17:31 11. juni til kl.03:05 12 juni
df1_datoer = df1[(df1['Tid(norsk normaltid)'] >= '2021-06-11 17:31') & (df1['Tid(norsk normaltid)'] <= '2021-06-12 03:05')]

#Sjkker om verdiene ser riktige ut
print(df1_datoer.head())

# Lager grafen
plt.figure(figsize=(10, 5))

# Legger i verdiene og tidene vi vil ha
plt.plot(df1_datoer["Tid(norsk normaltid)"], df1_datoer["Lufttemperatur"], label="Lufttemperatur (Fil 1)", color='blue')

# Gir grafen navn og setter x og y
plt.xlabel("Dato og tid")
plt.ylabel("Temperatur (°c)")
plt.title("Temperaturfall kveld og natt 11 og 12 juni")
plt.legend()
plt.show()