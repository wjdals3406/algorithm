import sys
n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
data2 = list(map(int, sys.stdin.readline().split()))

info = dict()
for i in data:
    info[i] = 0

# ����Ʈ�� append�ؼ� �ѹ��� ����ϴ� �ͺ��� �̷��� ���ڿ��� �ѹ��� ����ϴ°� �� ����
result = ''
for i in data2:
    if i in info:
        result += '1 '
    else:
        result += '0 '
print(result)
    