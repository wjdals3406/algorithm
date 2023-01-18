def main():
 
    string = input()    # ��ü ���ڿ�
    bomb = input()      # ���� ���ڿ�
 
    lastChar = bomb[-1] # ���� ���ڿ��� ������ ����
    stack = []
    length = len(bomb)  # ���� ���ڿ��� ����
 
    for char in string:
        stack.append(char)
        if char == lastChar and ''.join(stack[-length:]) == bomb:
            del stack[-length:]
 
    answer = ''.join(stack)
 
    if answer == '':
        print("FRULA")
    else:
        print(answer)
 
 
if __name__ == '__main__':
    main()
