N=int(input())
p=[]
for i in range(2,N):
    for j in range(2,i):
        if i%j==0:
            break
        else:
            if i%j!=0 and i+j==N:
                b=str(j)+' '+str(i)
                p.append(str(b))
print(p[-1])
