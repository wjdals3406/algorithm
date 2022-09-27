# -*- coding: utf-8 -*-
import sys
s = sys.stdin.readline().rstrip()
t = list(sys.stdin.readline().rstrip())
while len(s) != len(t):
    if t.pop() == 'B':
        t.reverse()
if s == ''.join(t):
    print(1)
else:
    print(0)
        
