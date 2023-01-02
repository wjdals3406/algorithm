def solution(people, limit):
    answer = 0
    people = sorted(people, reverse=True)
    
    s,e = 0,len(people) - 1
    while s <= e:
        if people[s] + people[e] > limit:
            answer += 1
            s += 1
        else:
            s += 1
            e -= 1
            answer += 1
    return answer