# from itertools import combinations
# �� Ǯ�̴� �ð��ʰ���
# sort�ؼ� �յ� �ܾ ���ϱ�
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