import sys
n,m = map(int, sys.stdin.readline().split())
data = dict()
data2 = dict()
for i in range(1,n+1):
    data[sys.stdin.readline().rstrip()] = i #dict(zip(pr[1:n+1], range(1, n+1))) 이렇게 한줄로 작성하는 방법도 있음
for i,v in data.items():
    data2[v] = i
    
result = ""
for _ in range(m):
    value = sys.stdin.readline().rstrip()
    if value.isalpha():
        result += str(data[value]) + "\n"
    elif value.isdigit():
        result += data2[int(value)] + "\n"
        
print(result)