import math

num = 600851475143
factor = 2
itr = 2
factorlst = []
pfactorlst = []

def factorfind(factor,num):
    while factor < num:
        if num%factor == 0:
	        factorlst.append(factor)
	        factor+=1
        else:
	        factor+=1

factorfind(factor, num)
print(factorlst)

def primfactorfind(factorlst, itr):
    for i in factorlst:
        while itr < math.sqrt(i):
            if itr != i:
                if i%itr != 0:
                    itr+=1
                else:
                    break
                pfactorlst.append(i)
            else:
                pfactorlst.append(i)

primfactorfind(factorlst,itr)
print(pfactorlst)
