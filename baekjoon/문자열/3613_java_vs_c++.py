# C++형식이라면 Java형식으로, Java형식이라면 C++형식으로 바꾸면 된다.
# 만약 C++형식과 Java형식 둘 다 아니라면, 에러를 발생시킨다. 변수명을 변환할 때, 단어의 순서는 유지
import sys
word = sys.stdin.readline().rstrip().split("_")

if len(word) > 1:
    answer = word[0]
    if "".join(word).lower() != "".join(word):
        answer = "Error!"
    else:
        for i in range(len(word)):
            if len(word[i]) == 0:
                answer = "Error!"
                break
            if i >= 1:
                answer += word[i].capitalize()
else:
    word = word[0]
    answer = ""
    s = 0
    for i in range(len(word)):
        c = word[i]
        # c가 대문자이면
        if c.isupper():
            if i == 0:
                answer = "Error!"
                break
            answer += word[s:i].lower() + "_"
            s = i
    if answer != "Error!":
        answer += word[s:].lower()

print(answer)
