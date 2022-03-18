import sys

n = int(sys.stdin.readline())
sort_list = [int(sys.stdin.readline()) for _ in range(n)]
sort_list.sort(reverse=True)
for i in sort_list:
    print(i, end = ' ')
    