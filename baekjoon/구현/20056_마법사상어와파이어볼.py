# -*- coding: utf-8 -*-
import sys
n,m,k = map(int, sys.stdin.readline().split())
data = list([[] for _ in range(n)] for _ in range(n)) #m,s,d

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
for _ in range(m):
    r,c,m,s,d = map(int, sys.stdin.readline().split())
    data[r-1][c-1].append((m,s,d))

def move():
    ndata = []
    for r in range(n):
        for c in range(n):
            if len(data[r][c]) > 0:
                for m,s,d in data[r][c]:
                    nr = (r + s*dx[d]) % n # 1��-N�� �� ����Ǿ��ֱ� ����
                    nc = (c + s*dy[d]) % n
                    ndata.append((nr,nc,m,s,d))
                data[r][c] = []
                
    for nr,nc,m,s,d in ndata:
        data[nr][nc].append((m,s,d))
    
def merge():
    for i in range(n):
        for j in range(n):
            if len(data[i][j]) >= 2:
                nm, ns = 0, 0
                eflag,oflag = 0,0
                for m,s,d in data[i][j]:
                    nm += m #3.1
                    ns += s #3.2
                    if d % 2 == 0: #������ ¦��
                        eflag = 1
                    else:
                        oflag = 1 #������ Ȧ��
                nm = nm // 5
                ns = ns // len(data[i][j])
                
                data[i][j] = []
                if nm == 0: #4 ������ 0�̸� �Ҹ�
                    continue
                #3.3
                if (eflag and not oflag) or (not eflag and oflag): #������ ��� Ȧ�� or ��� ¦��
                    for k in range(0,7,2): #���� ¦�� 
                        data[i][j].append((nm,ns,k))
                      
                else: 
                    for k in range(1,8,2): #���� Ȧ��
                        data[i][j].append((nm,ns,k))
                

for _ in range(k):
    move()
    merge()
res = 0
for i in range(n):
    for j in range(n):
        if len(data[i][j]) >= 1:
            for m,_,_ in data[i][j]:
                res += m
print(res)
            
            
# N, M, K = map(int, input().split())
# fireballs = []
# for _ in range(M):
#     _r, _c, _m, _s, _d = list(map(int, input().split()))
#     fireballs.append([_r-1, _c-1, _m, _s, _d])

# MAP = [[[] for _ in range(N)] for _ in range(N)]

# dx = [-1, -1, 0, 1, 1, 1, 0, -1]
# dy = [0, 1, 1, 1, 0, -1, -1, -1]

# for _ in range(K):
#     # ���̾ �̵�
#     while fireballs:
#         cr, cc, cm, cs, cd = fireballs.pop(0)
#         nr = (cr + cs * dx[cd]) % N  # 1��-N�� �� ����Ǿ��ֱ� ����
#         nc = (cc + cs * dy[cd]) % N
#         MAP[nr][nc].append([cm, cs, cd])

#     # 2�� �̻����� üũ
#     for r in range(N):
#         for c in range(N):
#             # 2�� �̻��� ��� -> 4���� ���̾�� �ɰ���
#             if len(MAP[r][c]) > 1:
#                 sum_m, sum_s, cnt_odd, cnt_even, cnt = 0, 0, 0, 0, len(MAP[r][c])
#                 while MAP[r][c]:
#                     _m, _s, _d = MAP[r][c].pop(0)
#                     sum_m += _m
#                     sum_s += _s
#                     if _d % 2:
#                         cnt_odd += 1
#                     else:
#                         cnt_even += 1
#                 if cnt_odd == cnt or cnt_even == cnt:  # ��� Ȧ���̰ų� ��� ¦���� ���
#                     nd = [0, 2, 4, 6]
#                 else:
#                     nd = [1, 3, 5, 7]
#                 if sum_m//5:  # ���� 0�̸� �Ҹ�
#                     for d in nd:
#                         fireballs.append([r, c, sum_m//5, sum_s//cnt, d])

#             # 1���� ���
#             if len(MAP[r][c]) == 1:
#                 fireballs.append([r, c] + MAP[r][c].pop())

# print(sum([f[2] for f in fireballs]))