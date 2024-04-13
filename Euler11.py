f =open('Euler11data.txt', 'r', encoding="utf-8")
list=f.read()
d=list.splitlines()
for i in range(20):
    d[i]=d[i].split(' ')
    for j in range(20):
        d[i][j]=int(d[i][j])
h=[]
for i in range(20):
    for j in range(20):
        h.append(d[i][j])
print(d)
print(h)
l=0
for i in range(17):
    for j in range(20):
        if d[i][j]*d[i+1][j]*d[i+2][j]*d[i+3][j] > l:
            l=d[i][j]*d[i+1][j]*d[i+2][j]*d[i+3][j]
for i in range(3,20):
    for j in range(20):
        if d[i][j]*d[i-1][j]*d[i-2][j]*d[i-3][j] > l:
            l=d[i][j]*d[i-1][j]*d[i-2][j]*d[i-3][j]
for i in range(20):
    for j in range(17):
        if d[i][j]*d[i][j+1]*d[i][j+2]*d[i][j+3] > l:
            l=d[i][j]*d[i][j+1]*d[i][j+2]*d[i][j+3]
for i in range(20):
    for j in range(3,20):
        if d[i][j]*d[i][j-1]*d[i][j-2]*d[i][j-3] > l:
            l=d[i][j]*d[i][j-1]*d[i][j-2]*d[i][j-3]
for i in range(17):
    for j in range(17):
        if d[i][j]*d[i+1][j+1]*d[i+2][j+2]*d[i+3][j+3] > l:
            l=d[i][j]*d[i+1][j+1]*d[i+2][j+2]*d[i+3][j+3]
for i in range(17):
    for j in range(3,20):
        if d[i][j]*d[i+1][j-1]*d[i+2][j-2]*d[i+3][j-3] > l:
            l=d[i][j]*d[i+1][j-1]*d[i+2][j-2]*d[i+3][j-3]
for i in range(3,20):
    for j in range(17):
        if d[i][j]*d[i-1][j+1]*d[i-2][j+2]*d[i-3][j+3] > l:
            l=d[i][j]*d[i-1][j+1]*d[i-2][j+2]*d[i-3][j+3]
for i in range(3,20):
    for j in range(3,20):
        if d[i][j]*d[i-1][j-1]*d[i-2][j-2]*d[i-3][j-3] > l:
            l=d[i][j]*d[i-1][j-1]*d[i-2][j-2]*d[i-3][j-3]

print (l)