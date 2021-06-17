def below_prime(n):
    for num in range(2, n):
    
     if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
          print(list(num))