import sys
x = int(sys.stdin.readline())

count = 0
num_list = [5, 3, 2]
while x != 1:
    for i in num_list:
        if (x-1)%i == 0:
            x -= 1
            count += 1
            break
        if x % i == 0:
            x /= i
            count += 1
            break
print(count)

# 이코테 풀이 답안 이해 안감
# d = [0] * 3001
# for i in range(2, x+1):
#     d[i] = d[i-1] +1
    
#     if i%2 == 0:
#         d[i] = min(d[i], d[i]//2) + 1
#     if i%3 == 0:
#         d[i] = min(d[i], d[i]//3) + 1
#     if i%5 == 0:
#         d[i] = min(d[i], d[i]//5) + 1
        
# print(d[x])
        

