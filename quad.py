import math
def solve_quadratic(a,b,c):
  a = int(input(" a: 1 ")
  b = int(input("b: 5 " )
  c = int(input("c:6")
  x**2 - 5 * x + 6 = 0
  d = b**2-4*a*c 
if d < 0:
    print ("NONE")
elif d == 0:
    x = (-b+math.sqrt(b**2-4*a*c))/2*a
    print (x)
else:
    x1 = (-b+math.sqrt(b**2-4*a*c))/2*a
    x2 = (-b-math.sqrt(b**2-4*a*c))/2*a
    print (x1 , x2)