import sys #���ʿ� �� ���� �� a[::-1]�� �� reverse�ؼ� �ִ� ����� ����
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