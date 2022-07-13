import sys
g = int(sys.stdin.readline()) #탑승구
p = int(sys.stdin.readline()) #비행기

airplane = [0 for _ in range(p+1)]
port = [[] for _ in range(g+1)]
for i in range(1, p+1):
    val = int(sys.stdin.readline())
    airplane[i] = val
    port[val].append(i)
    
for i in range(1, p+1):
    for j, jv in enumerate(port[airplane[i]]):    
        airplane[jv+1] -= 1
        port[j-1] += port[1:]
        port[j] = port[1]
        
