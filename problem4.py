num1 = 100
num2 = 100
multiplylist = []
palindromelist = []

def multiply1(num1, num2):
    while num1 < 1000:
	    x = num1*num2
	    multiplylist.append(x)
	    num1+=1

def multiply2(num1, num2):
    while num2 < 1000:
	    multiply1(num1, num2)
	    num2+=1

multiply2(num1, num2)

def palindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False

def palincheck(multiplylist):
    for i in multiplylist:
        if palindrome(i) == True:
            palindromelist.append(i)

palincheck(multiplylist)
print(palindromelist.sort())
