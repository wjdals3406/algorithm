def make_short(s, l):
    answer = ""
    pre = s[:l]
    cnt = 1
    
    for i in range(l,len(s), l):
        if pre == s[i:i+l]:
            cnt += 1
        else:
            if cnt >= 2:
                answer += str(cnt) + pre
            else:
                answer += pre
                
            pre = s[i:i+l]
            cnt = 1
    
    if cnt >= 2:
        answer += str(cnt) + pre
    else:
        answer += pre
    
    return len(answer)

def solution(s):
    answer = len(s)
    
    for i in range(1,len(s)//2+1):
        answer = min(answer, make_short(s, i))
    
    return answer