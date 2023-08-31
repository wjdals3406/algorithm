import sys
# 상근이가 방문한 빌딩의 번호가 들어간 순서대로
n, q = map(int, sys.stdin.readline().split())
data = [int(sys.stdin.readline()) for _ in range(q)]
ground = [0] * (n+1)


def func(p):
    # 부모를 거슬러 올라갔을 때 선점한 땅에 도착하지 않으면 0 return
    num = p
    visited = 0
    while p != 0:
        if ground[p] == -1:  # 누가 미리 선점한 상태
            visited = p  # 여기서 return해주는 것이 아니라 값을 계속 변경해줘야 함..
        p //= 2

    if visited > 0:
        return visited
    else:
        ground[num] = -1
        return visited


for num in data:
    print(func(num))
