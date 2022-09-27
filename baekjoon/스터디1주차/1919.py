import sys
from collections import Counter
a = sys.stdin.readline().rstrip()
adic = dict(Counter(a))
b = sys.stdin.readline().rstrip()
bdic = dict(Counter(b))

result = 0
for i in adic:
    if i in b:
        result += abs(adic[i] - bdic[i])
    else:
        result += adic[i]

for i in bdic:
    if i not in a:
        result += bdic[i]
print(result)