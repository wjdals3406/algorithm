def rotate(map_list, r, c, n, m): #리스트 값 회전
    change_matrix = [[0] * n for _ in range(m)]
    for i in range(n): 
        for j in range(m):
            change_matrix[j][m - 1 - i] = map_list[i][j]
    cur_r = c
    cur_c = r

    tmp = m
    m = n
    n = tmp

    return change_matrix, cur_r, cur_c , n, m


if __name__== "__main__":
    n, m = map(int, input().split())
    c, r, d = map(int, input().split())

    map_list = []
    for _ in range(n):
        map_list.append(list(map(int, input().split()))) 
#------------여기까지가 입력값--------------
    visit = [[0] * m for _ in range(n)] #가본 곳 체크위해 모두 false로 초기화 (0이 안가본 곳)

    # direction = [1, 2, 3] #동서남북 -> 현재값 변경
    # for i in range(3): #위치와 방문여부 리스트 rotate
    #     if direction[i] == d:
    #         for j in range(4-i):
    #             map_list, cur_r, cur_c = rotate(map_list, r, c)
    #             visit, r, c = rotate(visit, r, c)

 
    #현재 위치는 가본 곳인가?
    #왼쪽에 가보지 않은 칸 존재(모서리가 아니고, 바다가 아니고, 안가봤고) -> 왼쪽 방향으로 회전 후 왼쪽으로 한 칸 전진
    count = 0
    while True:
        if r>0 and map_list[r][c-1] != 1 and visit[r][c-1] != 0:
            map_list, r, c, n, m = rotate(map_list, r, c, n, m) #왼쪽으로 회전
            
            c -= 1 #왼쪽으로 전진
            visit[r][c-1] = 0 # 가본 곳 체크
            count+=1


        else: #왼쪽 방향에 가보지 않은 칸이 없다면(왼쪽이 바다 or 모서리 or 가봄) 모서리 어떻게 처리해?
            if c>0:
                if map_list[r][c-1] != 1 or visit[r][c-1] != 1:
                    map_list, r, c, n, m = rotate(map_list, r, c, n, m)
                    continue
            
            if c<m:
                if map_list[r][c+1] != 1 or visit[r][c+1] != 1:
                    map_list, r, c, n, m = rotate(map_list, r, c, n, m)
                    continue

            if r>0:
                if map_list[r-1][c] != 1 or visit[r-1][c] != 1:
                    map_list, r, c, n, m = rotate(map_list, r, c, n, m)
                    continue

            if r<n:
                if map_list[r+1][c] != 1 or visit[r+1][c] != 1:
                    map_list, r, c, n, m = rotate(map_list, r, c, n, m)
                    continue
            

            if map_list[r+1][c] == 1: #뒤쪽 방향이 바다
                break

            r += 1
            count+=1

                    
            # check_map = [map_list[r][c-1], map_list[r][c+1], map_list[r-1][c], map_list[r+1][c]]
            # check_visit = [visit[r][c-1], visit[r][c+1], visit[r-1][c], visit[r+1][c]]

            # if sum(check_map) == 4 and sum(check_visit) == 4:
            #     if map_list[r+1][c] == 1: #뒤쪽 방향이 바다
            #         count+=1
            #         break

            #     for _ in range(2):
            #         map_list, r, c, n, m = rotate(map_list, r, c)
            # else:
            #     map_list, r, c, n, m = rotate(map_list, r, c)
            # continue

print(count)