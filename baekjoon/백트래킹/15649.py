# -*- coding: utf-8 -*-
#�ߺ����� : product
#�ߺ����� : combinations_with_replacement
import sys
from itertools import combinations_with_replacement
n,m = map(int, sys.stdin.readline().split())
data = [i for i in range(1,n+1)]
for i in list(combinations_with_replacement(data, m)):
    print(*i)