# -*- coding: utf-8 -*-
from collections import defaultdict
def solution(commands):
    answer = []
    data = [[[0,0] for _ in range(5)] for _ in range(5)] #category값, 병합여부
    dic = defaultdict(list)
    
    for i in commands:
        com = i.split()
        if com[0] == 'UPDATE':
            if len(com) == 4:
                r,c,value = int(com[1]), int(com[2]), com[3]
                if data[r][c][0] == 0:
                    data[r][c][0] = value
                    dic[value].append((r,c))
                else:
                    dvalue = data[r][c][0]
                    for r_,c_ in dic[dvalue]:
                        data[r_][c_][0] = value
                    dic[value].extend(dic[dvalue])
                    del dic[dvalue]
                        
                    
            elif len(com) == 3:
                value,change = com[1],com[2]
                dic[change] = dic[value]
                del dic[value]
                for r,c in dic[change]:
                    data[r][c][0] = change
                    
        elif com[0] == 'MERGE':
            r1,c1,r2,c2 = int(com[1]),int(com[2]),int(com[3]),int(com[4])
            if r1 == r2 and c1 == c2:
                continue
            
            if data[r1][c1][0] == 0 and data[r2][c2][0] != 0:
                value = data[r2][c2][0]
                data[r1][c1][0] = data[r2][c2][0]
                data[r1][c1][1],data[r2][c2][1] = 1,1
                dic[value].append((r1,c1))
            elif data[r1][c1][0] != 0 and data[r2][c2][0] == 0:
                value = data[r1][c1][0]
                data[r2][c2][0] = data[r1][c1][0]
                data[r1][c1][1],data[r2][c2][1] = 1,1
                dic[value].append((r2,c2))
                
            elif data[r1][c1][0] != 0 and data[r2][c2][0] != 0: #merge된거에 + merge할 수 있음
                #merge값도 달라야 하나..? 그냥 0,1이 아니라??
                value = data[r2][c2][0]
                data[r2][c2][0] = data[r1][c1][0]
                
                
                
                dic[value].remove((r2,c2))
                dic[data[r1][c1][0]].append((r2,c2))
                data[r1][c1][1],data[r2][c2][1] = 1,1
            
        elif com[0] == 'UNMERGE':
            r,c = int(com[1]),int(com[2])
            value = data[r][c][0]
            rlist = []
            for ri,ci in dic[value]:
                if data[ri][ci][1] == 1:
                    data[ri][ci][0] = 0
                    data[ri][ci][1] = 0
                    rlist.append((ri,ci))
            for ri, ci in rlist:
                dic[value].remove((ri,ci))
            
            if value != 0:
                data[r][c][0] = value
                dic[value].append((r,c))
                
        elif com[0] == 'PRINT':
            r,c = int(com[1]),int(com[2])
            if data[r][c][0] == 0:
                answer.append("EMPTY")
            else:
                answer.append(data[r][c][0])
    print(data)
    print(dic)
    
    return answer

commands = ["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]
print(solution(commands))