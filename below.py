def is_prime(n):
   if n>1:
       for i in range (2, n):
           if n % i == 0 :
               return "False"
               break
       else:
            return "True"
   else:
        return "False"


   def primes_below(n):
    for i in range(2, n + 1):
        if is_prime(i):
            print(i, end = " ")