c11,c21=map(str,input().split())
yas1=0
if len(c11)>len(c21):
  c11,c21=c21,c11
p1=0
while p1<len(c11):
  yas1+=(ord(c21[p1])-ord(c11[p1]))
  p1+=1
for p1 in range(p1,len(c21)):
  yas1+=ord(c21[p1])-ord('a')+1
print(yas1)
