n = 1
length = [0,0]

def collatz(n):
    l = 0
    while n != 1:
        if n%2 == 0:
            n=n/2
        else:
            n=3*n+1
        l+=1
    return l

while n < 1000000:
    if collatz(n) > length[0]:
        length[0] = collatz(n)
        length[1] = n
    n+=1

print(length)
