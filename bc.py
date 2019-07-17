a=int(input())
b=input("")
c=list(bb.split(" "))
c.sort(reverse=True)
b=list(map(int,c))
if sum(b)==0:
  print("0")
else:
  d="".join(c)
  print(d)
