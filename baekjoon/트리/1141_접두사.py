import sys
n = int(sys.stdin.readline())
data = [sys.stdin.readline().rstrip() for _ in range(n)]
data.sort()
        
idx,cnt = 0,0
while idx < len(data):
    if idx + 1 < len(data) and data[idx+1].startswith(data[idx]):
        idx += 1
    else:
        idx += 1
        cnt += 1

print(cnt)
        