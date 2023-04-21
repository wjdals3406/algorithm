def find_p(data):
    answer = []
    for i in range(5):
        for j in range(5):
            if data[i][j] == "P":
                answer.append((i,j))
    
    return answer

def distance(p1,p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def check_is_ok(p_loc, data):
    for i in range(len(p_loc)):
        for j in range(i+1,len(p_loc)):
            dist = distance(p_loc[i],p_loc[j])
            
            if dist == 1:
                return 0
            elif dist == 2:
                p1, p2 = p_loc[i] , p_loc[j]
                maxX = p1[0] if p1[0] > p2[0] else p2[0]
                maxY = p1[1] if p1[1] > p2[1] else p2[1]
                minX = p1[0] if p1[0] < p2[0] else p2[0]
                minY = p1[1] if p1[1] < p2[1] else p2[1]
                for r in range(minX, maxX+1):
                    for c in range(minY, maxY+1):
                        if data[r][c] == "O":
                            return 0
    return 1                
    
def solution(places):
    answer = []
    
    #맨해튼 거리가 1이면 무조건 안됨 / 맨해튼 거리가 2일 때 경우의 수가 생김
    for case in places:
        p_loc = find_p(case)
        answer.append(check_is_ok(p_loc, case))
    
    
    return answer