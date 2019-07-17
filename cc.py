n = int(input())
a,s = [],0
for i in range(0,n):
  a.append(list(map(int,input().split())))
  s += a[i][(n-1)-i]
print(s)
