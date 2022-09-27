import sys
n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
a, b = map(int, sys.stdin.readline().split())
result = 0

for i in range(n):
    if data[i] - a > 0:
        data[i] = data[i] - a
        result += 1
        if data[i] % b != 0:
            result += data[i] // b + 1
        else:
            result += data[i] // b
    else:
        result += 1
print(result)
    