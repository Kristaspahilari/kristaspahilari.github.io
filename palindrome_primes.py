a = 10000
b = 99999
a += 1
l = []
for num in range(a,b):
    if(str(num) == str(num)[::-1]):
        if(num>1):
            for a in range(2,num):
                if(num%a==0):
                    y = False
                    break
            else:
                l.append(num)
                print(l)

