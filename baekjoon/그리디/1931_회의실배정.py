# -*- coding: utf-8 -*-
import sys
n = int(sys.stdin.readline())
#���۽ð��� ������ �ð��� �������� �־���
data = [tuple(map(int,sys.stdin.readline().split())) for _ in range(n)]
data = sorted(data, key=lambda x : (x[1], x[0]))
res = 1
etime = data[0][1]
for s,e in data[1:]:
    if etime <= s:
        etime = e
        res += 1
print(res)
 