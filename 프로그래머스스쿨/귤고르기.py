from collections import Counter
#�̰� �ߺ��������� Ǯ�� �ð��ʰ��� -> �ð����⵵ �����غ���
def solution(k, tangerine):
    #value������ ����
    data = sorted(Counter(tangerine).items(), key=lambda x: x[1])
    cnt = 0
    k = len(tangerine) - k
    for idx, val in enumerate(data):
        key, value = val
        k -= value
        if k == 0:
            return len(data) - idx - 1
        elif k < 0:
            return len(data) - idx
            
    return 0