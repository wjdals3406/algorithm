#����Ʈ �� �ٷ� ����ϴ� ��� -> ����Ʈ �տ� *�� ���̱�
#' '.join()�� ���ڿ����� �ش�Ǵ� ���̱� ������ int���� ������
import sys
n = int(sys.stdin.readline())
student = [i for i in range(1, n+1)]
data = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    d = student.pop(i)
    student.insert(i - data[i], d)

print(*student)