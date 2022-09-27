#가장 인접한 두 공유기 사이의 거리의 최댓값을 구하는 문제
#가장 인접한 두 공유기 사이의 거리를 조절해 나가며 
# C(공유기 개수)보다 많은 개수로 공유기를 설치할 수 있으면 거리를 증가시키고
# C보다 적은 개수로 공유기를 설치할 수 있으면 거리를 증가시킨다.

n, c = list(map(int, input().split(' ')))

# 전체 집의 좌표 정보를 입력 받기
array = []
for _ in range(n):
     array.append(int(input()))
array.sort() 

start = 1 # 가능한 최소 거리(min gap)
end = array[-1] - array[0] # 가능한 최대 거리(max gap)
result = 0

while(start <= end): # 이진 탐색으로 가장 인접한 두 공유기 사이의 거리를 탐색함
    mid = (start + end) // 2 # 가장 인접한 두 공유기 사이의 거리(gap)
    # 첫째 집에는 무조건 공유기를 설치한다고 가정 -> why? 중간에 공유기 설치하는 것보다 첫번째집에 설치하는게 거리가 더 클 수 밖에 없어서?
    value = array[0]
    count = 1
    for i in range(1, n): # 앞에서부터 차근차근 설치 
        if array[i] >= value + mid: #설치한 곳 + gap
            value = array[i]
            count += 1
    if count >= c: # C개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가시키기
        start = mid + 1
        result = mid # 최적의 결과를 저장
    else: # C개 이상의 공유기를 설치할 수 없는 경우, 거리를 감소시키기
        end = mid - 1

print(result)