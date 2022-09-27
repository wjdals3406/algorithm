import sys
num = int(sys.stdin.readline())
fib = [0 for _ in range(num+1)]
def fibo(n):
    if fib[n] != 0:
        return fib[n]
    if n <= 1:
        fib[n] = n
    else:
        fib[n] = fibo(n-1) + fibo(n-2)
    return fib[n]

print(fibo(num))