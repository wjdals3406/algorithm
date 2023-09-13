import sys
from itertools import combinations
n = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = int(1e9)

for case in combinations(range(n), n//2):
    other_team = [i for i in range(n) if i not in case]
    # 각 팀에서 두 명씩 뽑고 S를 구해야 함
    ctotal = ototal = 0
    for cteam in combinations(case, 2):
        ctotal += data[cteam[0]][cteam[1]]
        ctotal += data[cteam[1]][cteam[0]]
    for oteam in combinations(other_team, 2):
        ototal += data[oteam[0]][oteam[1]]
        ototal += data[oteam[1]][oteam[0]]
    answer = min(abs(ototal - ctotal), answer)
    if answer == 0:
        break
print(answer)
