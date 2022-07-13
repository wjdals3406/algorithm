from bisect import bisect_left
import sys

def binary_search(array, target, start, end):
    mid = (start + end) // 2
    if start > end :
        return -1
    
    if array[mid] == mid:
        return mid
    
    elif array[mid] < mid:
        return binary_search(array, mid, mid + 1, end)
    else:
        return binary_search(array, mid, start, mid - 1)

n = int(sys.stdin.readline())
data = list(map(int,sys.stdin.readline().rstrip().split()))
print(binary_search(data, data[n-1], 0, n-1))


# flag = 0
# for i in data:
#     if bisect_left(data, i) == i:
#         print(i)
#         flag = 1
#         break
    
# if flag == 0:
#     print(-1)