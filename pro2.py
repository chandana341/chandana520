from itertools import combinations
Na,ka=map(int,input().split())
a1=len(str(Na))
lst=list(combinations(str(Na),a1-ka))
lst=sorted(lst)
print(*lst[0],sep='')
