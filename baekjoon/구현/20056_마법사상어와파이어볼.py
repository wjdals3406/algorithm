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
                    nr = (r + s*dx[d]) % n 
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
                    if d % 2 == 0: #¹æÇâÀÌ Â¦¼ö
                        eflag = 1
                    else:
                        oflag = 1 #¹æÇâÀÌ Â¦¼ö
                nm = nm // 5
                ns = ns // len(data[i][j])
                
                data[i][j] = []
                if nm == 0: #4 Áú·®ÀÌ 0ÀÌ¸é ¼Ò¸ê
                    continue
                #3.3
                if (eflag and not oflag) or (not eflag and oflag): #¹æÇâÀÌ ¸ğµÎ È¦¼ö or ¸ğµÎ Â¦¼ö
                    for k in range(0,7,2): #¹æÇâ Â¦¼ö 
                        data[i][j].append((nm,ns,k))
                      
                else: 
                    for k in range(1,8,2): #¹æÇâ È¦¼ö
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
            