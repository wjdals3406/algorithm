import sys
n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
data2 = list(map(int, sys.stdin.readline().split()))

info = dict()
for i in data:
    info[i] = 0

# 리스트에 append해서 한번에 출력하는 것보다 이렇게 문자열로 한번에 출력하는게 더 빠름
result = ''
for i in data2:
    if i in info:
        result += '1 '
    else:
        result += '0 '
print(result)
    