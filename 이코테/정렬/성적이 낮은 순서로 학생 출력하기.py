import sys

n = int(sys.stdin.readline())

sort_list = [list(map(str,sys.stdin.readline().split())) for _ in range(n)]
sort_list.sort(key=lambda x:x[1]) 
for i in sort_list:
    print(i[0], end = ' ')
    
 


    