import sys
n = int(sys.stdin.readline())
data = []

for _ in range(n):
    word = sys.stdin.readline().rstrip()
    sum = 0
    for i in word:
        if i.isdigit():
            sum += int(i)
    data.append((word, sum))
    
data = sorted(data, key = lambda x : (len(x[0]), x[1], x[0]))
for i in data:
    print(i[0])