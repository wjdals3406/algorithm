def solution(routes):
    routes.sort(key = lambda x : x[1]) #�ִ��� ���� ���� ���� ���� ����
    
    cnt = 1
    camera = routes[0][1]
    
    for s,e in routes[1:]:
        if camera < s:
            camera = e
            cnt += 1
            
    return cnt