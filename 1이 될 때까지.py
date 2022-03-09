import sys
n, k = map(int,sys.stdin.readline().split())

count = 0
while True:
    if n%k == 0:
        n /= k
    else:
        n -= 1

    count += 1

    if n==1:
        break

print(count)

