# -*- coding: utf-8 -*-
import sys
word = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()
res = ""
wrd_list = []
w_len, b_len = len(word), len(bomb)
s = 0
if bomb in word:
    while s <= w_len - b_len: 
        if word[s] != bomb[0]:
            if wrd_list:
                res += ''.join(wrd_list)
                wrd_list = []
            while s <= w_len - 1 and word[s] != bomb[0]: #bomb�� ù�ܾ ���ö����� for������ �߰�
                res += word[s]
                s += 1
        if s >= w_len:
            break 
        cnt = 0
        for i in range(b_len): #bomb �ܾ �ִ��� Ȯ��
            if word[s] != bomb[i]:
                break
            s += 1
            cnt += 1
        
        if cnt < b_len:#bomb �ܾ� ����
            wrd_list.append(word[s - i:s])
        else:
            if wrd_list: #bomb�ܾ� ����
                a = b_len - len(wrd_list[-1])
                if wrd_list[-1] + word[s:s+a] == bomb: #while������ �ݺ� ������
                    while len(wrd_list) > 0 and wrd_list[-1] + word[s:s+a] == bomb:
                        a = b_len - len(wrd_list[-1])
                        wrd_list.pop()
                        s = s+a
                    # s = s - a
                else:
                    res += ''.join(wrd_list)
                    wrd_list = []
    if wrd_list:
        if wrd_list[-1] + word[s:] != bomb:
            res += ''.join(wrd_list) + word[s:]
            wrd_list = []
    else:
        res += word[s:]
                    
    if len(res) == 0:
        print("FRULA")
    else:
        print(res)
else:
    print(word)
            

    
        