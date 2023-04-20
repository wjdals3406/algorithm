def check(s):
    stack = []
    for i in range(len(s)):
        if s[i] == "(":
            stack.append("(")
        else:
            if stack:
                stack.pop()
            else:
                return 0
    if stack:
        return 0
    
    return 1

def split_char(s):
    o,e = 0,0
    for i in range(len(s)):
        if s[i] == "(":
            o += 1
        else:
            e += 1
        if o == e:
            return s[:i+1], s[i+1:]

def reverse_char(s):
    answer = ''
    for i in range(len(s)):
        if s[i] == "(":
            answer += ")"
        else:
            answer += "("
    
    return answer

def make(p):
    u,v = '', ''
    if len(p) == 0:
        return p
    
    #u,v�� �и�
    u,v = split_char(p)
    
    if check(u): #u�� �ùٸ� ��ȣ ���ڿ�
        return u + make(v)
    else:#u�� �ùٸ� ��ȣ ���ڿ��� �ƴ� ��
        answer = "("
        answer += make(v)
        answer += ")"
        answer += reverse_char(u[1:-1])
        return answer
    
def solution(p):
    
    if len(p) == 0 or check(p):
        return p
    
    return make(p)