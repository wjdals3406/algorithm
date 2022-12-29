# -*- coding: utf-8 -*-
import sys
# ÆøÅºÀÌ ÀÖ´Â Ä­ -> 3ÃÊ ÈÄ¿¡ Æø¹ß
# ÆøÅºÀÌ Æø¹ßÇÑ ÀÌÈÄ -> ÆøÅºÀÌ ÀÖ´ø Ä­ ÆÄ±« -> ºó Ä­, ÀÎÁ¢ÇÑ ³× Ä­µµ ÇÔ²² ÆÄ±«
# ÆøÅºÀÌ Æø¹ßÇßÀ» ¶§, ÀÎÁ¢ÇÑ Ä­¿¡ ÆøÅºÀÌ ÀÖ´Â °æ¿ì¿¡´Â ÀÎÁ¢ÇÑ ÆøÅº Áï½Ã ÆÄ±«
# ÆøÅº ¼³Ä¡ -> 1ÃÊ µ¿¾È Á¤Áö -> 1ÃÊµ¿¾È ÆøÅº ¼³Ä¡µÇÁö ¾ÊÀº ¸ðµç Ä­¿¡ ÆøÅº ¼³Ä¡

r,c,n = map(int, sys.stdin.readline().split())
data = [list(map(str, list(sys.stdin.readline().rstrip()))) for _ in range(r)]
time = [[3 for _ in range(c)] for _ in range(r)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def spend_time():
    global n
    if n == 0:
        return
    n -= 1
    
    for x in range(r):
        for y in range(c):
            if data[x][y] == 'O':
                time[x][y] -= 1
            
def install_bomb():
    if n == 0:
        return
    for x in range(r):
        for y in range(c):
            if data[x][y] != 'O':
                data[x][y] = 'O'
    spend_time()

def explode():
    rm = []
    for x in range(r):
        for y in range(c):
            if time[x][y] == 0:
                time[x][y] = 3
                data[x][y] = '.'
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or nx >= r or ny < 0 or ny >= c:
                        continue
                    if data[nx][ny] == 'O':
                        rm.append((nx,ny))
                        
                    else:
                        data[nx][ny] = '.'
                        time[nx][ny] = 3
    for x,y in rm:
        data[x][y] = '.' 
        time[x][y] = 3

spend_time()
install_bomb()
spend_time()
explode()
while n > 0:
    install_bomb()
    if n == 0:
        break
    explode()
    spend_time()
    

for i in data:
    print(''.join(i))
    
