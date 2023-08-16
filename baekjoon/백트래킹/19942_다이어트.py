import sys
from itertools import combinations
n = int(sys.stdin.readline())
nutrient = list(map(int, sys.stdin.readline().split()))
flist = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
answer_price = int(1e9)
answer_comb = []
for i in range(1, n+1):
    for case in combinations(range(n), i):
        a = b = c = d = price = 0
        for idx in case:
            a += flist[idx][0]
            b += flist[idx][1]
            c += flist[idx][2]
            d += flist[idx][3]
            price += flist[idx][4]
            if answer_price < price:
                break

            if a >= nutrient[0] and b >= nutrient[1] and c >= nutrient[2] and d >= nutrient[3]:
                if answer_price > price:
                    answer_price = price
                    answer_comb = [case]
                elif answer_price == price:
                    answer_comb.append(case)

if answer_price == int(1e9):
    print(-1)
else:
    print(answer_price)
    for i in sorted(answer_comb)[0]:
        print(i+1, end=" ")

# import sys
# import copy
# n = int(sys.stdin.readline())
# nutrient = list(map(int, sys.stdin.readline().split()))
# flist = [list(map(int, sys.stdin.readline().split())) + [i+1]
#          for i in range(n)]
# flist.sort(key=lambda x: x[4])
# res = int(1e9)
# rlist = []
# answer = []


# def dfs(idx, total):
#     global res, answer
#     if idx == n:
#         return

#     for i in range(idx, n):
#         for j in range(4):
#             nutrient[j] -= flist[i][j]
#         rlist.append(flist[i][-1])
#         total += flist[i][4]

#         if max(nutrient) <= 0:
#             if res > total:
#                 res = total
#                 answer = sorted(copy.copy(rlist))
#             elif res == total:
#                 tmp = sorted(copy.copy(rlist))
#                 if tmp < answer:
#                     answer = tmp

#             for j in range(4):
#                 nutrient[j] += flist[i][j]
#             rlist.pop()
#             return

#         dfs(i+1, total)
#         total -= flist[i][4]
#         for j in range(4):
#             nutrient[j] += flist[i][j]
#         rlist.pop()


# dfs(0, 0)
# if res == int(1e9):
#     print(-1)
# else:
#     print(res)
#     print(*answer)
