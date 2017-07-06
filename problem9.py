a = 1
b = 1
c = 1

def checkfunc(a,b,c):
    if a**2+b**2==c**2:
        print(a,b,c,a+b+c)
        if a+b+c==1000:
            print(a, b, c)
            print(a*b*c)
            break
        else:
            return False
    else:
        return False

def aitr(a, b, c):
    while a+b+c <= 1000:
        if checkfunc(a,b,c) == False:
            a+=1

def bitr(a, b, c):
    while a+b+c <= 1000:
        if checkfunc(a,b,c) == False:
            aitr(a, b, c)
            a = 1
            b+=1

def citr(a, b, c):
    while a+b+c <= 1000:
        if checkfunc(a,b,c) == False:
            bitr(a,b,c)
            b = 1
            c+=1

citr(a,b,c)
