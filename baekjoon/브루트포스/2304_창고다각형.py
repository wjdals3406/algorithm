# 기둥들의 위치와 높이가 주어질 때, 가장 작은 창고 다각형의 면적 구하기
# max 높이까지는 계속 높이가 올라가야하고
import sys
n = int(sys.stdin.readline())
stack = sorted([list(map(int, sys.stdin.readline().split()))
               for _ in range(n)])
height = stack[0][1]
answer = i = 0
for l in stack:
    if l[1] > answer:
        answer = l[1]
        idx = i
    i += 1

for i in range(idx):
    if height < stack[i+1][1]:
        answer += height * (stack[i+1][0] - stack[i][0])
        height = stack[i+1][1]
    else:
        answer += height * (stack[i+1][0] - stack[i][0])

height = stack[-1][1]
for i in range(n-1, idx, -1):
    if height < stack[i-1][1]:
        answer += height * (stack[i][0] - stack[i-1][0])
        height = stack[i-1][1]
    else:
        answer += height * (stack[i][0] - stack[i-1][0])

print(answer)
