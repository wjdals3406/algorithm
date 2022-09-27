import sys
n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
data.sort()
s = 0
e = n-1
count = 0
while s < e:
    if data[s] + data[e] == m:
        s += 1
        e -= 1
        count += 1
    elif data[s] + data[e] > m:
        e -= 1
    elif data[s] + data[e] < m:
        s += 1
    

print(count)
        
        