def below_prime(n):
    l = []
    for num in range(2, n):
     if num > 1:
    
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
          l.append(num)
          print(l)