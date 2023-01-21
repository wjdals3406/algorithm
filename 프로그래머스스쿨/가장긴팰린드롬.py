# -*- coding: utf-8 -*-
def solution(s):

    def is_palindrome(word):
        if word == word[::-1]:
            return len(word)
        else: return -1
    
    maxval = 0
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            word_len = is_palindrome(s[i:j])
            if word_len != -1:
                maxval = max(maxval, word_len)

    return maxval


print(solution("abcdcba"))