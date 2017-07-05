factors = 0
y=7733
triangles = []

def factornum(n):
    x = 2
    f = [1]
    while x <= n:
        if n%x == 0:
            f.append(x)
        x+=1
    return len(f)

def triangle(n):
    if len(triangles) == 0:
        t = sum(list(range(1,n)))
    else:
        t = n+triangles[-1]
    return t

while factors<=500:
    factors = factornum(triangle(y))
    y+=1
    print(y," ",factors)

print(triangle(y-1))
