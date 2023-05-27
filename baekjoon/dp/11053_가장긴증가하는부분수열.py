import sys
n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
count = [1] * n

for i in range(n):
    for j in range(i-1, -1, -1):
        if data[i] > data[j]:
            if count[i] <= count[j]:
                count[i] = count[j] + 1
print(max(count))
