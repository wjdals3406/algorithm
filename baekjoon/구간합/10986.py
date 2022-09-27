import sys
n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
sumval = [0]
sum = 0
count = 0
for i in data:
    sum += i
    if i % m == 0:
        count += 1
    if sum % m == 0:
        count += 1
    sumval.append(sum)

for i in range(2, n+1):
    for j in range(1,n-i+1):
        if (sumval[j+i] - sumval[i-1]) % m == 0:
            count += 1
print(count)