#�ּ� �ʿ� �Ƿε� : �ش� ������ Ž���ϱ� ���� ������ �־�� �ϴ� �ּ����� �Ƿε�
#�Ҹ� �Ƿε� : ������ Ž���� �� �Ҹ�Ǵ� �Ƿε�
#dungeons�� ������ 10�� �����̱� ������ �ð��ʰ� �ȳ�
from itertools import permutations
def solution(k, dungeons):
    answer = 0
    
    for i in list(permutations(dungeons, len(dungeons))):
        total = k
        res = 0 
        for need, remove in i:
            if total >= need:
                total -= remove
                res += 1
            else:
                break
        answer = max(answer, res)
    return answer