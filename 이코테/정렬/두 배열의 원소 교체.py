import sys

#A의 가장 작은 원소와 B의 가장 큰 원소를 switch
n, k = list(map(int,sys.stdin.readline().split()))
a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))
a.sort()
b.sort()
print(sum(a[k:]) + sum(b[-k:]))
    
