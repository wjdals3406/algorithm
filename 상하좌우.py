import sys
N = input()
dir = list(map(str,sys.stdin.readline().split()))

cur_row = 1
cur_col = 1
row = [0, 0, -1, 1]
col = [-1, 1, 0, 0]
loc = ['L', 'R', 'U', 'D']

for i in dir:
    for j in range(4):
        if i == loc[j]:
            cur_row += row[j]
            cur_col += col[j]
            if cur_row < 1 or cur_col <1:
                cur_row -= row[j]
                cur_col -= col[j]
            
print(cur_row, cur_col)
