import sys
n = int(sys.stdin.readline())
data = [int(sys.stdin.readline()) for _ in range(n)]
data.sort(reverse=True)
res = 0
for i in range(n-1, -1, -1):
    res = max(res, data[i] * (i+1))
print(res)