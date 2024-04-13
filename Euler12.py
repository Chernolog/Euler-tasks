import math
def factors(x):
    factors_list=[]
    for i in range (2, math.floor(math.sqrt(x)+1)):
        if x % i == 0:
            factors_list.append(i)
            factors_list.append(x//i)
    return factors_list
print(factors(28), len(factors(28)))
b=1
i=1
while len(factors(b)) <=500:
    i+=1
    b+=i
print (b)
print (len(factors(b)))
print (factors(b))