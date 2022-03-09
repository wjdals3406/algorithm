import sys
n, k = map(int,sys.stdin.readline().split())

count = 0
while True:
    if n%k == 0:
        n /= k
    else:
        n -= 1

    count += 1

    if n==1:
        break

print(count)

#이게 숫자가 커지면 비효율적이라는데 좋은 방법 생각해보기, 이코테 코드도 이해해보기
