import sys
import math
n = int(sys.stdin.readline())
data = list(map(int,sys.stdin.readline().split()))
count = 0
for i in data:
    if i == 1:
        continue
    flag = 0
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        count += 1
print(count)
    