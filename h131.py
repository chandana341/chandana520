inter=int(input())
a1=list(map(int,input().split()))
d=sorted(a1)
k1=d[::-1]
p1=[]
for i in range(0,len(a1)):
    p1.append(k1[i])
    p1.append(d[i])
for j in p1[:len(a1)]:
    print(j,end=" ")
