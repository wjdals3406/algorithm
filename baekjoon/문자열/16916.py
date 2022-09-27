import sys
word = sys.stdin.readline().rstrip()
p = sys.stdin.readline().rstrip()
print(1) if p in word else print(0)
