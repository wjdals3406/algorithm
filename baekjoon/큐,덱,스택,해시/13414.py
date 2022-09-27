import sys
k,l = map(int, sys.stdin.readline().rstrip().split())
wait = dict()
for _ in range(l):
    student = sys.stdin.readline().rstrip()
    if student in wait:
        del wait[student]
        wait[student] = 0
    else:
        wait[student] = 0

count = 0
for key,val in wait.items():
    print(key)
    count += 1
    if count == k:
        break