class Triangle():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
      s=(self.a + self.b + self.c)/2
      return (s*((s-self.a)*(s-self.b)*(s-self.c)))** 0.5
    
    def perimeter(self):
        return self.a + self.b + self.c 
    
    def is_valid(self):
        if self.a + self.b >= self.c:
            return True 
        elif self.b + self.c >= self.a:
            return True 
        elif self.a + self.c >= self.b:
           return True 
        else:
            return False
    
    def is_right(self):
        if self.a**2+self.b**2==self.c**2:
            return True
        else:
            return False

        