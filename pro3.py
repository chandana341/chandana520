a1,b1=input().split()
char=abs(len(b1)-len(a1))
for g in range(len(a1)):
  if(len(b1)==1 and b[g] in a1):
    break
  if(a[g1]!=b[g1]):
    char=char+1
print(char)
