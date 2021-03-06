n = 2
prim = []

def isprime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

def primlist(n):
    while n < 2000000:
        if isprime(n) == True:
    	    prim.append(n)
        n+=1

primlist(n)
suml = sum(prim)
print(suml)
