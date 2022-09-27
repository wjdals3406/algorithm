import sys
n = int(sys.stdin.readline())
re = 0
num = 666
i=0
while True:
    if '666' in str(num):
        re += 1
    if re == n:
        break
    num += 1
    i+=1
    
print(num)
print(i)