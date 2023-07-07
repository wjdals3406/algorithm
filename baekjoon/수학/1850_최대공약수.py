import sys
a, b = map(int, sys.stdin.readline().split())
# 두 수의 최대공약수만큼 1 반복
# 최대공약수 구하는 방법 -> 유클리드 호제법


def func(a, b):
    while b > 0:
        a, b = b, a % b

    return a * '1'


if a > b:
    print(func(a, b))
else:
    print(func(b, a))
