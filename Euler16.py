x=2**1000
d=0
while x != 0:
    d += x % 10
    x = x // 10
print(d)