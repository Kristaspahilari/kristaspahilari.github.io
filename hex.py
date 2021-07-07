def to_hex(n):
    if (n < 0):
        return 0
    elif (n<=1):
     return n 
    else:
        to_hex ( n / 16 )
        x =(n%16)
        if (x < 10):
            print(x), 
        if (x == 10):
            print("A"),
        if (x == 11):
            print("B"),
        if (x == 12):
            print("C"),
        if (x == 13):
            print("D"),
        if (x == 14):
            print("E"),
        if (x == 15):
            print ("F")

def hex_color(r, g, b):
  return  ('{:X}{:X}{:X}').format(r, g, b)

print(hex_color(10,32,255))


