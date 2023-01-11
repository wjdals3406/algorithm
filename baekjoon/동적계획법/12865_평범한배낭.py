import sys
n,k = map(int, sys.stdin.readline().split())
dp = [0] * (k+1)
for _ in range(n):
    w,v = map(int, sys.stdin.readline().split())
    for i in range(k, w-1, -1):
        dp[i] = max(dp[i-w] + v, dp[i])
print(dp[-1])

# import sys
# from itertools import combinations

# n,k = map(int, sys.stdin.readline().split())
# data = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
# data.sort(key = lambda x : x[0])
# maxval = 0
# for i in range(1, n+1):
#     for j in list(combinations(data, i)):
#         ksum = 0
#         vsum = 0
#         for s in j:
#             ksum += s[0]
#             vsum += s[1]
#             if ksum > k:
#                 break
#         if ksum > k:
#             break
        
#         maxval = max(maxval, vsum)
# print(maxval)
    
    
    



