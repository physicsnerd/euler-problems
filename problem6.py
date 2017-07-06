n = 1
n2 = 1
tot1 = 0
tot2 = 0

def squarer(n):
    while n < 101:
        global tot1
        tot1 = tot1 + n**2
        n+=1

squarer(n)

def addnsquare(n2):
    while n2 < 101:
        global tot2
        tot2 = tot2 + n2
        n2+=1
    tot2 = tot2**2

addnsquare(n2)

fin = tot2-tot1
print(fin)
