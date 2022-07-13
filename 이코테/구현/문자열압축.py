# -*- coding: utf-8 -*-
word = input()
result = ""
count = 1
idx = 0
minval = len(word)

for s in range(1,len(word) // 2 + 1): #split ¥‹¿ß
    count = 1
    idx = 0
    result = ""
    while idx < len(word):
        if word[idx:idx+s] == word[idx+s:idx+2*s]: #abc/abc/abc/ab
            while word[idx:idx+s] == word[idx+s:idx+2*s]:
                count += 1
                idx += s
            result += str(count) + word[idx:idx+s]
            count = 1
        else:
            result += word[idx:idx+s]
        idx += s
    if len(result) < minval:
        minval = len(result)

print(minval)