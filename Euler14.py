def Collatz(x):
    num=1
    d=[]
    while x != 1:
        if x % 2 == 0 :
            x = x // 2
        else:
            x = 3*x + 1
        num+=1
        d.append(x)
    return (num, d)
print (Collatz(13)[0])
x=1
y=1
for i in range(1,10**6):
    if Collatz(i)[0] > x:
        x=Collatz(i)[0]
        y=i
print(x,y)
