def solution(routes):
    routes.sort(key = lambda x : x[1]) #최대한 지점 끝에 놓는 것이 유리
    
    cnt = 1
    camera = routes[0][1]
    
    for s,e in routes[1:]:
        if camera < s:
            camera = e
            cnt += 1
            
    return cnt