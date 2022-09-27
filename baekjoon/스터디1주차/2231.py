import sys
n = int(sys.stdin.readline())
flag = 0
if n > 55:
    for i in range(n - 55, n+1):
        data = list(str(i))
        data = [int(i) for i in data]
        if i + sum(data) == n:
            flag = 1
            print(i)
            break
else:
    for i in range(1, n):
        data = list(str(i))
        data = [int(i) for i in data]
        if i + sum(data) == n:
            flag = 1
            print(i)
            break
if flag == 0:
    print(0)