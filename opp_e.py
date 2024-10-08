# Oppgave e)
import pandas as pd

###### Fil 1: temperatur_trykk_met_samme_rune_time_datasett.csv.txt 
def les_fil1(filnavn):
    # Leser CSV-filen
    df1 = pd.read_csv(filnavn, sep=';', header=0)
    # Skriver ut temperatur fra Lufttemperatur
    print(df1["Lufttemperatur"])
    # Gjør om tid(norsk normaltil) til datetime-formatet dag, måned, år, timer og minutter
    df1["Tid(norsk normaltid)"] = pd.to_datetime(df1["Tid(norsk normaltid)"], format="%d.%m.%Y %H:%M")

    # Bytter ut (,) med (.) og gjør om til float på lufttemperatur og lufttrykk i havnivå
    df1["Lufttemperatur"] = df1["Lufttemperatur"].str.replace(',', '.').astype(float)
    df1["Lufttrykk i havnivå"] = df1["Lufttrykk i havnivå"].str.replace(',', '.').astype(float)

    return df1

###### Fil 2: trykk_og_temperaturlogg_rune_time.csv.txt
def les_fil2(filnavn):
    # Leser CSV-filen filnavn --> bane, sep=";" --> atskilt med (;) og header=0 --> Gjør at linje 0 til ikke blir bruk som data 
    df2 = pd.read_csv(filnavn, sep=';', header=0)

    # Gjør om Dato og tid til datetime-formatet, error="coarce" --> Hvis det er en verdi som ikke kan konverteres så bytter den den ut med Nat 
    df2["Dato og tid"] = pd.to_datetime(df2["Dato og tid"], errors='coerce')
    df2 = df2.dropna(subset=["Dato og tid"]) # Gjør at gyldige rader beholdes

    # Bytter ut (,) med (.) og gjør om til float på trykk og temperatur
    df2["Trykk - barometer (bar)"] = df2["Trykk - barometer (bar)"].str.replace(',', '.').astype(float)
    df2["Trykk - absolutt trykk maaler (bar)"] = df2["Trykk - absolutt trykk maaler (bar)"].str.replace(',', '.').astype(float)
    df2["Temperatur (gr Celsius)"] = df2["Temperatur (gr Celsius)"].str.replace(',', '.').astype(float)

    # Fyller in de verdiene som mangler i Trykk - barometer med gjennomsnittet av verdiene
    df2["Trykk - barometer (bar)"] = df2["Trykk - barometer (bar)"].fillna(df2["Trykk - barometer (bar)"].mean())

    return df2

# For å vise at filene blir riktig lest og behandlet.
if __name__ == "__main__": # Gjør at koden kan importeres uten at dette blir tatt med.

    # Setter argumentene til filene og gjør dem til df1 og df2
    df1 = les_fil1('temperatur_trykk_met_samme_rune_time_datasett.csv.txt')
    df2 = les_fil2("trykk_og_temperaturlogg_rune_time.csv.txt")

    # Skriver de første radene av fil 1
    print(df1.head()) # Brukt for å teste koden

    # Skriver de første radene av fil 2
    print(df2.head()) # Brukt for å teste koden