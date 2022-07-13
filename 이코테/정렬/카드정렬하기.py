# -*- coding: utf-8 -*-
import sys

n = int(sys.stdin.readline())
card = []
for _ in range(n):
    card.append(int(sys.stdin.readline()))
card.sort()

# sum = 0
# for i in range(len(card)):
#     if i < 2:
#         sum += card[i]*(len(card)-1)
#     else:
#         sum += card[i]*(len(card)- i)
# print(sum)

    
# import heapq
# import sys

# N = int(input())
# card_deck = []
# for _ in range(N):
#     heapq.heappush(card_deck, int(sys.stdin.readline()))


# if len(card_deck) == 1: #1개일 경우 비교하지 않아도 된다
#     print(0)
# else:
#     answer = 0
#     while len(card_deck) > 1: #1개일 경우 비교하지 않아도 된다
#         temp_1 = heapq.heappop(card_deck) #제일 작은 덱
#         temp_2 = heapq.heappop(card_deck) #두번째로 작은 덱
#         answer += temp_1 + temp_2 #현재 비교 횟수를 더해줌
#         heapq.heappush(card_deck, temp_1 + temp_2) #더한 덱을 다시 넣어줌
    
#     print(answer)