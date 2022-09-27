import sys
import math
m, n = map(int,sys.stdin.readline().split())
data = [True for _ in range(n+1)]

for i in range(2, int(math.sqrt(n)) + 1):
    if data[i]:
        re = 2
        while i * re <= n:
            data[i*re] = False
            re += 1
            
for i in range(m, n+1):
    if i <=1:
        continue
    if data[i]:
        print(i)

        