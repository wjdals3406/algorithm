def solution(s):
    answer = []
    for string in s:
        count, idx, stack = 0, 0, ""
        while idx < len(string):            # 110 ã��
            if string[idx] == "0" and stack[-2:] == "11":
                stack = stack[:-2]
                count += 1
            else:
                stack += string[idx]
            idx += 1

        idx = stack.find("111")             # 110�� ���� string���� 111 ã��
        if idx == -1:                       # 0�ڿ� 110 �ݺ��� ���̱�
            idx = stack.rfind('0')
            stack = stack[:idx+1]+"110"*count+stack[idx+1:]
        else:                               # 111�տ� 110 �ݺ��� ���̱�
            stack = stack[:idx]+"110"*count+stack[idx:]
        answer.append(stack)
    return answer

print(solution(["1110","100111100","0111111010"]))