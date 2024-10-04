def datatilliste_sola():
    time, temp, pres = [], [], []
    with open('temperatur_trykk_met_samme_rune_time_datasett.csv.txt', 'r') as f:
        a = f.readlines()
        for i in a[1:-1]:
            j = i.replace(',' , '.')
            x = j.split(';')
            time.append(x[2])
            temp.append(float(x[3]))
            pres.append(float(x[4][:-1]))
    return(time, temp, pres)




print(datatilliste_sola())