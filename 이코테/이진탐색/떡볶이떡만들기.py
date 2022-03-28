import sys
def make_total(array, target_value):
    total = 0
    for i in array:
        if target_value > i:
            continue
        total += (i - target_value)
        
    return total
        
def binary_search(array, m, total, start, end): #target = m, start와 end는 모두 값(인덱스 아님)
    search_value = (start + end) // 2
    total = make_total(array, search_value)
    if total >= m and make_total(array, search_value + 1) < m:
        return search_value
    elif total < m:
        return binary_search(array, m, total, search_value, end)
    elif total > m:
        return binary_search(array, m, total, start, search_value)
        
    
n, m = map(int,sys.stdin.readline().split())
length_list = list(map(int,sys.stdin.readline().split()))
length_list.sort()

search_index  = (0 + n - 1) // 2

total = make_total(length_list, length_list[search_index])
if total == m:
    print(length_list[search_index])
elif total < m:#왼쪽 인덱스로 작아질때까지 이동
    while total < 6:
        search_index += 1
        total = make_total(length_list, length_list[search_index])
        
    print(binary_search(length_list, 6, total, length_list[search_index], length_list[search_index + 1])) #array, target, start, end
    

elif total > m: #오른쪽으로 작아질 때까지 인덱스 이동
    while total > 6:
        search_index += 1
        total = make_total(length_list, length_list[search_index])
        
    print(binary_search(length_list, 6, total, length_list[search_index - 1], length_list[search_index])) #array, target, start, end
    

    