# from itertools import combinations
# 내 풀이는 시간초과남
# sort해서 앞뒤 단어를 비교하기
def solution(phone_book):
    # data = list(combinations(phone_book,2))
    # for a,b in data:
    #     if a.startswith(b) or b.startswith(a):
    #         return False
    for p in range(len(phone_book)):
        for l in range(p+1,len(phone_book)):
            if phone_book[p].startswith(phone_book[l]) or phone_book[l].startswith(phone_book[p]):
                return False
        
    return True