import sys
word = sys.stdin.readline().rstrip()
data = [word[i:] for i in range(len(word))]
print('\n'.join(sorted(data)))