from itertools import permutations
na,ma=map(int,input().split())
da=list(map(int,input().split()))
for i in permutations(da,2):
    if(sum(i)==ma):
        print("yes")
        break
else:
    print("no")
