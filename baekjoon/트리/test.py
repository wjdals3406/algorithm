def adjacent(x): # x�� i �� ������ ���� ������ �ٵ� for���� ���� x�� i�� ���� ���� ����.
    for i in range(x): #�ε����� ��  row[n]���� ��
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i: # ���� ���ų� �밢���� ������ false
            return False # �밢���� �������� �� ��ǥ���� �� - �� = �� - �� �� ������ �ΰ��� ���� �밢���� �ִ�.
    return True
 
#���پ� ����ϸ� dfs ����
 
def dfs(x):
    global result
 
    if x == N:
        result += 1
    else:
        # �� �࿡ �� ����
        for i in range(N): # i �� ����ȣ 0���� N ������ �Űܰ��鼭 �����Ѱ� ã��
            row[x] = i
            if adjacent(x): # ��,��,�밢�� üũ�Լ� true�̸� ��Ʈ��ŷ ���ϰ� ��� ����
                dfs(x + 1)
 
# N = int(input())/
N = int(input())
row = [0] * N
result = 0
print(row)
dfs(0)
# print(row)
print(result)