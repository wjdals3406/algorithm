#리스트 한 줄로 출력하는 방법 -> 리스트 앞에 *을 붙이기
#' '.join()은 문자열에만 해당되는 것이기 때문에 int형은 에러남
import sys
n = int(sys.stdin.readline())
student = [i for i in range(1, n+1)]
data = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    d = student.pop(i)
    student.insert(i - data[i], d)

print(*student)