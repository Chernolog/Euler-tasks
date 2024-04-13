f =open('input.txt', 'r', encoding="utf-8")
list=f.read()
list=list.splitlines()
print (list)
x=0
for i in range(100):
    x+=int(list[i])
print(x)