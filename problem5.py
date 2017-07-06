num = 2
itr = 2

while itr < 21:
    if num%itr == 0:
        itr+=1
    else:
        num+=1
        itr = 2

print(num)
