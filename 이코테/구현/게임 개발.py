r, c = map(str, input().split())
cur_y, cur_r, d = map(str, input().split())

map_list = []
for i in range(r):
    map_list.append(list(map(int, input().split())))


#현재 위치에서 왼쪽 방향을 바라봄 -> 안가본 칸 있음 왼쪽으로 회전 후 왼쪽으로 한 칸 전진
#                                   가본 칸이면 왼쪽 방향으로 회전만 수행

for ridx, row in enumerate(map_list):
    for cidx in range(4):
        if cur_r == ridx and cur_y == cidx: #현재 위치로 이동
            if cidx > 1:


            else :
                if row[cidx] == 1


