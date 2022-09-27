import sys #애초에 값 넣을 때 a[::-1]로 값 reverse해서 넣는 방법도 있음
data = []
info = sys.stdin.readline().rstrip().split()
n = int(info[0])
cnt = len(info) - 1
info.pop(0)
while cnt < n:
    data = sys.stdin.readline().rstrip().split()
    info.extend(data)
    cnt += len(data)

info = list(map(lambda x : int(''.join(reversed(x))), info))
info.sort()
for i in info:
    print(i)