from collections import defaultdict
def solution(genres, plays):
    answer = []

    dic = defaultdict(list)
    for g,p in zip(genres, plays):
        dic[g].append(p)

    #속한 노래가 많이 재생된 값 기준으로 장르 정렬
    data = sorted(dic.items(), key = lambda x : -sum(x[1]))
    for i in range(len(data)):
        play = sorted(data[i][1])
        cnt = 0
        while play:
            #장르 별 두개씩만 append
            if cnt == 2:
                break

            num = play.pop()

            #plays 배열에서 num값이 unique 하지 않을 때
            if plays.count(num) > 1:
                for j in range(len(plays)):
                    if plays[j] == num and genres[j] == data[i][0]:
                        if j in answer:
                            continue
                        answer.append(j)
                        break
            else:
                answer.append(plays.index(num))

            cnt += 1
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))


#다른 사람의 풀이
# def solution(genres, plays):
#     answer = []
    
#     d = defaultdict(list)
#     for g,p,i in zip(genres, plays, range(len(plays))):
#         d[g].append([p,i])
            
#     genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
#     for g in genreSort:
#         temp = [e[1] for e in sorted(d[g],key= lambda x: (-x[0], x[1]))]
#         answer += temp[:min(len(temp),2)]
#     return answer

# def solution(genres, plays):
#     answer = []

#     dic1 = defaultdict(list)
#     dic2 = defaultdict(list)
    
#     for g,p,i in zip(genres, plays, range(len(plays))):
#         dic1[g].append([i,p])
#         dic2[g].append(p)

#     for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
#         for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:
#             answer.append(i)

#     return answer