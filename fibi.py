def big_fibonacci(m):
    l = []
    a = 1 
    b = 1
    while True:
        c = a + b
        a = b
        b = c
        for item in b:
            m = str(item)
            n = len(str(item))
            print(n)

        