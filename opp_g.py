import statistics as s

def average(time, temp, n):
    
    for i in range(n):
        time.pop(0)
        time.pop(-1)
        
    temp_temp = []
    temp_out = []
    for i in range(2*n+1):
        temp_temp.append(temp[i])    
    temp_out.append(s.mean(temp_temp))
    for i in range(len(time)-1):
        temp_temp.pop(0)
        temp_temp.append(temp[2*n+1+i])
        temp_out.append(s.mean(temp_temp))

    return time, temp_out
