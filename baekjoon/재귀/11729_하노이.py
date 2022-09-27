import sys
n = int(sys.stdin.readline())

result = 0
def hanoi(n, one, two, three, result):
    result += 1
    if n == 1:
        return result
    # elif n == 2:
    #     print(1, 2)
    elif n > 1:
        hanoi(n-1, one, two, three, result)
        print(one)
        print(two)
        print(three)
        hanoi(n-1, result)
        # print(n, 2)
        # hanoi(n-1, result)
        # print(n-1, 3)
    return result
hanoi(n,result)