def datatilliste_sola():
    time, temp, pres = [], [], []
    with open('temperatur_trykk_met_samme_rune_time_datasett.csv.txt', 'r') as f:
        a = f.readlines()
        for i in a[1:-1]:
            j = i.replace(',' , '.')
            x = j.split(';')
            time.append(x[2])
            temp.append(float(x[3]))
            pres.append(float(x[4]))
    return(time, temp, pres)

def datatilliste_uis():
    time, temp, pres, pres_a = [], [], [], []
    with open('trykk_og_temperaturlogg_rune_time.csv.txt', 'r') as f:
        a = f.readlines()
        for i in a[1:]:
            j = i.replace(',' , '.')
            x = j.split(';')
            time.append(x[0])
            temp.append(float(x[4]))
            pres.append(float(x[3]))
            if x[2] == '':
                pres_a.append('')
            else:
                pres_a.append(float(x[2]))
    return(time, temp, pres, pres_a)

