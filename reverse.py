def my_reverse(list):
    m = 0            
    n = len(list)-1   
    while m<n:
        list[m],list[n] = list[n],list[m]
        m += 1
        n -= 1
    return list