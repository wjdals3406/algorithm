from collections import defaultdict
def solution(genres, plays):
    answer = []

    dic = defaultdict(list)
    for g,p in zip(genres, plays):
        dic[g].append(p)

    data = sorted(dic.items(), key = lambda x : -sum(x[1]))
    for i in range(len(data)):
        play = sorted(data[i][1])
        cnt = 0
        while play:
            if cnt == 2:
                break

            num = play.pop()

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