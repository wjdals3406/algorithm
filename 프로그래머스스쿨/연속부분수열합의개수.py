def solution(elements):
    res = []
    elements = elements*2
    elements.pop()
    
    for i in range(len(elements)):
        s,e = 0,i+1
        t = sum(elements[s:e])
        res.append(t)
        while e < len(elements):
            t -= elements[s]
            t += elements[e]
            print(t)
            
            s += 1
            e += 1
            res.append(t)
    
    return len(set(res))

print(solution([7,9,1,1,4]))