def Solve(x):
    for i in range(1,x):
        for j in range(i+1,x):
            k=x-i-j
            if (i**2 + j**2 == k**2):
                return i*j*k
print (Solve(1000))

## Testing