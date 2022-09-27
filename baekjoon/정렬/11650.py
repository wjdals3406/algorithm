import sys
n = int(sys.stdin.readline())
data = []
for _ in range(n):
    a,b = map(int, sys.stdin.readline().split())
    data.append((a,b))
data = sorted(data, key = lambda x : (x[0], x[1]))
for a,b in data:
    print(a,b)
    
# import sys

# lst = sys.stdin.readlines()[1:]
# lst.sort(key=lambda x: int(x.split()[1]))
# lst.sort(key=lambda x: int(x.split()[0]))
# print(''.join(lst))