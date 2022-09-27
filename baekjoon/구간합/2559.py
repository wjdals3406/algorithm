import sys
n, k = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
sumval = [0]
sum = 0
for i in data:
    sum += i
    sumval.append(sum)

maxval = -int(1e9)    
for i in range(k, n+1):
    maxval = max(maxval, sumval[i] - sumval[i-k])
print(maxval)
