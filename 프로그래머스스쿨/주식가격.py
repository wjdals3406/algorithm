from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        p = prices.popleft()
        cnt = 0
        for i in prices:
            cnt += 1
            if i < p:
                break
        answer.append(cnt)
        
    return answer