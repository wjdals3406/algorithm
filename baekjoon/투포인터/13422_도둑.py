import sys
t = int(sys.stdin.readline())
#n : 집의 개수 / m개 연속, k미만

for _ in range(t):
    n, m, k = map(int, sys.stdin.readline().split())
    money = list(map(int, sys.stdin.readline().split()))
    cnt = 0
    
    if n == m:
        if sum(money) < k:
            print(1)
        else:
            print(0)
    else:
    
        sumval = sum(money[:m])
        s,e = 0, m
        
        while s < n:
            if sumval < k:
                cnt += 1
            
            sumval -= money[s]
            sumval += money[e]
            
            s = s + 1
            e = (e + 1) % n
        
        print(cnt)
        
        