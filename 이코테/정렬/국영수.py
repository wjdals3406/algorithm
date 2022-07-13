import sys

n = int(sys.stdin.readline())
sort_list = []
for _ in range(n):
    sort_list.append(list(map(str,sys.stdin.readline().split())))
    
sort_list.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for i in range(n):
    print(sort_list[i][0])