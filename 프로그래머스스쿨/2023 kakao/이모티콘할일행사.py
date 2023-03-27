from itertools import product
def solution(users, emoticons):
    discount = [0.1, 0.2, 0.3, 0.4]
    case = list(product(discount, repeat=len(emoticons))) #중복순열
    
    def check(ratio,total,dcase):
        res = 0
        for emo,emeony in enumerate(emoticons):
            if ratio > dcase[emo] :
                continue
                
            #일정 비율 이상 할인하는 이모티콘을 모두 구매
            res += emeony * (1 - dcase[emo])
            
        if res >= total: #이모티콘 구매 비용의 합이 일정 가격 이상이 된다면, 이모티콘 구매를 모두 취소하고 이모티콘 플러스 서비스에 가입
            return 1, 0
        else:
            return 0, res
    
    answer = []
    for c in case:
        ecount, emoney = 0,0
        for ratio, total in users:
            cnt, money = check(ratio * 0.01, total, c)
            ecount += cnt
            emoney += money
        answer.append((ecount,emoney))
    
    answer.sort(reverse=True)    
    return answer[0]

users = [[40, 10000], [25, 10000]]	
emoticons = [7000, 9000]	
solution(users, emoticons)