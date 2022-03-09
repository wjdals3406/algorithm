import sys

# 선택한 행에서 뽑은 가장 숫자가 제일 크도록
n, m = map(int,sys.stdin.readline().split())
array_list = []

for i in range(n):
    num_list = list(map(int,sys.stdin.readline().split()))
    array_list.append(num_list)
    
min_list = []

for i, v in enumerate(array_list):
    min_list.append(min(v))

print(max(min_list))


#이코테 답 예시 -> 한번에 for문에서 해결하기
# max함수로 두 개의 값 비교 가능하다는 점 알기
# result = 0
# for i in range(n):
#     data = list(map(int, input().split()))
#     min_value = min(data)
#     result = max(result, min_value)

