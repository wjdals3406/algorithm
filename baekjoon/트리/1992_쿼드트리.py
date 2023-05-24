import sys
n = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
res = ""

def recursive(startX, startY, len): #4등분함
    global res
    
    if len < 1:
        return
    
    check = [row[startY:startY+len] for row in data[startX:startX + len]]
    if sum(map(sum, check)) == 0:
        res += '0'
    elif sum(map(sum, check)) == len**2:
        res += '1'
    else:
        #네 등분의 합을 구해보기
        coord = [(startX, startY), (startX, startY + len//2), (startX + len//2, startY), (startX + len//2, startY + len//2)]
        for idx,value in enumerate(coord):
            x,y = value
            split_data = [row[y:y+len//2] for row in data[x:x + len//2]]
            if idx == 0:
                res += '('
                
            if sum(map(sum, split_data)) == 0:
                res += '0'
            elif sum(map(sum, split_data)) == (len//2)**2:
                res += '1'
            else:
                recursive(x, y, len//2)
            
            if idx == 3:
                res += ')'
            

recursive(0, 0, n)
print(res)