import sys
from collections import Counter
n,c = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
cnt = sorted(Counter(data).items(), key = lambda x :(-x[1])) 

for a,b in cnt:
    print((str(a) + " ") * b, end = "")
    

