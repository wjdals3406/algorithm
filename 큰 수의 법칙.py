#배열의 크기 N
#숫자가 더해지는 횟수 M
# K

N, M, K = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort(reverse=True) #큰 수를 얻기 위해 sort

sum = 0
K_copy = K

while (M > 0):
    max_num= num_list[0]
    sec_num = num_list[1]

    while(M > 0 and K > 0):
        sum +=  max_num
        M = M - 1
        K = K - 1
    K = K_copy

    if M > 0:
        sum+=sec_num
        M = M -1

        
print(sum)
