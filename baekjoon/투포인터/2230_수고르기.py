import sys
n,m = map(int, sys.stdin.readline().split())
data = []
for _ in range(n):
    data.append(int(sys.stdin.readline()))
    
data.sort()
s,e = 0,1

res = int(2e9)
gap = int(2e9)
while e < n:
    while data[e] - data[s] >= m and s < e:
        gap = data[e] - data[s]
        s += 1
    res = min(res, gap)
    e += 1
print(res)
