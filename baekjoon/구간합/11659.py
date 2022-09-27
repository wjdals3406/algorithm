import sys
n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
sumval = [0]
sum = 0
for i in data:
    sum += i
    sumval.append(sum)
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(sumval[j] - sumval[i-1])