import sys
n, k = map(int, sys.stdin.readline().split())
money = []
for i in range(n):
    money.append(int(sys.stdin.readline()))  
    
result = 0
for i in range(n-1, -1, -1):
    if (k % money[i]) < k:
        result += (k // money[i])
        k %= money[i]
    if k <=0:
        break
print(result)
    