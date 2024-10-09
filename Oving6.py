import matplotlib.pyplot as plt
from statistics import mean
from datetime import datetime

def datatilliste_sola():
    time, temp, pres = [], [], []
    with open('temperatur_trykk_met_samme_rune_time_datasett.csv.txt', 'r') as f:
        a = f.readlines()
        for i in a[1:-1]:
            i = i.replace(',' , '.')
            x = i.split(';')
            time.append(x[2])
            temp.append(float(x[3]))
            pres.append(float(x[4]))
    return(time, temp, pres)


def datatilliste_uis():
    time, temp, pres, pres_a = [], [], [], []
    with open('trykk_og_temperaturlogg_rune_time.csv.txt', 'r') as f:
        a = f.readlines()
        for i in a[1:]:
            if i[2] != '/':
                i = i.replace(',' , '.')
                i = i.replace('am', 'AM')
                i = i.replace('pm', 'PM')
                x = i.split(';')
                time.append(x[0])
                temp.append(float(x[4]))
                pres.append(float(x[3]))
                if x[2] == '':
                    pres_a.append('')
                else:
                    pres_a.append(float(x[2]))
            else:
                break
    return(time, temp, pres, pres_a)


def average(time, temp, n):
    time_out = [x for x in time]
    for i in range(n):
        time_out.pop(0)
        time_out.pop(-1)
    temp_temp = []
    temp_out = []
    for i in range(2*n+1):
        temp_temp.append(temp[i])    
    temp_out.append(mean(temp_temp))
    for i in range(len(time_out)-1):
        temp_temp.pop(0)
        temp_temp.append(temp[2*n+1+i])
        temp_out.append(mean(temp_temp))
    return(time_out, temp_out)


def string_to_datetime(string, uis):
    if uis == True:
        for i in range(len(string)):
            string[i] = datetime.strptime(string[i], '%m.%d.%Y %H:%M')
    else:
        for i in range(len(string)):
            string[i] = datetime.strptime(string[i], '%d.%m.%Y %H:%M')
    return(string)


sola_str, sola_temp, sola_pres = datatilliste_sola()
sola_x = string_to_datetime(sola_str, False)

uis_str, uis_temp, uis_pres, uis_pres_a = datatilliste_uis()
uis_x = string_to_datetime(uis_str, True)

avg_x, avg_t = average(uis_x, uis_temp, 30)

temp_max = max(uis_temp[:6000])
temp_min = min(uis_temp[:6000])
max_i = uis_temp.index(temp_max)
min_i = uis_temp.index(temp_min)

plt.plot(uis_x, uis_temp)
plt.plot(avg_x, avg_t)
plt.plot(sola_x, sola_temp)
plt.plot([uis_x[max_i], uis_x[min_i]], [temp_max, temp_min])
plt.show()

uis_pres = [10*x for x in uis_pres]
uis_x_a = []
uis_pres_ab = []
ind = 0
for i in uis_pres_a:
    if i != '':
        uis_pres_ab.append(i)
        uis_x_a.append(uis_x[ind])
    ind += 1
uis_pres_ab = [10*x for x in uis_pres_ab]


plt.plot(uis_x, uis_pres)
plt.plot(uis_x_a, uis_pres_ab)
plt.plot(sola_x, sola_pres)
plt.show()