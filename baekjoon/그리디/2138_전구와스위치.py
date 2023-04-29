import sys
import copy
n = int(sys.stdin.readline())
data = list(sys.stdin.readline().rstrip())
result = list(sys.stdin.readline().rstrip())

def change(data, i):
    if data[i] == '1':
        data[i] = '0'
    else: data[i] = '1'
    
def check(data, result):
    cnt = 0
    for i in range(1, len(data)):
        if result[i-1] != data[i-1]:
            change(data, i-1)
            change(data, i)
            if i < len(data)-1:
                change(data, i+1)
            
            cnt += 1
    
    if data != result: return int(1e9)
    else: return cnt
            
#맨 처음에 버튼을 눌렀을 때와 안눌렀을 때          
data_cpy =copy.deepcopy(data)
    
one = check(data_cpy, result)
change(data,0)
change(data,1)
two = check(data, result)

res = min(one,two+1)

if res >= int(1e9):
    print(-1)
else:
    print(res)