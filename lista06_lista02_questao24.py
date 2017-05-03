list=[]
j=99
for i in range (100):
    x=int(input())
    list.append(x)
    soma=0
for i in range (50):
    a=list[i]
    b=list[j]
    soma+=(a-b)**3
    j-=1
print(soma)