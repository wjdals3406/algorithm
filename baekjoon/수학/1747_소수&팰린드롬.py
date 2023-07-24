#N보다 크거나 같고, 소수이면서 팰린드롬인 수 중에서 가장 작은 수
import sys
import math
n = int(sys.stdin.readline())

if n == 1: print(2)
else:
    for num in range(n, int(1e9)):
        flag = 0
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                flag = 1
                break
            
        if not flag:
            num_list = list(str(num))
            if num_list[::-1] == num_list:
                print(num)
                break
        