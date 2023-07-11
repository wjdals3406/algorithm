import sys
import copy
word = sys.stdin.readline().rstrip()
alphacount = [[0 for _ in range(26)]]
print = sys.stdout.write

for i, v in enumerate(word):
    sumlist = alphacount[i]
    appendlist = copy.copy(sumlist)
    index = ord(v) - ord('a')
    appendlist[index] += 1
    alphacount.append(appendlist)

n = int(sys.stdin.readline())
for _ in range(n):
    al, l, r = map(str, sys.stdin.readline().split())
    l = int(l)
    r = int(r)
    index = ord(al) - ord('a')
    print(f'{alphacount[r+1][index] - alphacount[l][index]}\n')
