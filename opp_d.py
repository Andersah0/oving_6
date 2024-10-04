def datatilliste_sola(data):
    time, temp, pres = [], [], []
    with open(data, 'r') as f:
        a = f.readlines()
        for i in a[1:-1]:
            j = i.replace(',' , '.')
            x = j.split(';')
            time.append(x[2])
            temp.append(float(x[3]))
            pres.append(float(x[4][:-1]))
    return(time, temp, pres)