n = input()

row = [str(i) for i in range(1,9)]
col = [chr(i) for i in range(97,105)]

row_mov = [2, -2, 1, -1]
col_mov = [1, -1, 2 ,-2]

cur_row = 0
cur_col = 0

count = 0
#a1을 (0,0)으로 둔다.
for i in range(8):
    if n[1] == row[i]:
        cur_row = i
    if n[0] == col[i]:
        cur_col = i
    
for i in range(len(row_mov)):
    for j in range(len(col_mov)):
        if (cur_row + row_mov[i] >-1) and (cur_col + col_mov[j] > -1):
            count += 1

print(count)
