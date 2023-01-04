def solution(rows, columns, queries):
    answer = []
    data = [[(i-1) * columns + j for j in range(1,columns+1)] for i in range(1,rows+1)]
    x1,y1,x2,y2 = queries[0]
    x1,y1,x2,y2 = x1-1,y1-1,x2-1,y2-1
    
    
    return data

rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(rows, columns, queries))