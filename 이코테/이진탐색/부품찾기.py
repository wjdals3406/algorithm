import sys

def binary_search(array, target, start, end):
    mid = (start + end) // 2
    if start > end :
        return "no"
    
    if array[mid] == target:
        return "yes"
    
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)
    else:
        return binary_search(array, target, start, mid - 1)
    
    
n = int(sys.stdin.readline().strip())
store = list(map(int,sys.stdin.readline().split()))
store.sort()

m = int(sys.stdin.readline().strip())
ask = list(map(int,sys.stdin.readline().split()))

for i in ask:
    print(binary_search(store, i, 0, n-1), end = ' ')

