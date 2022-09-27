res = 0
def fibo1(n):
    global res
    res += 1
    if n == 1 or n == 2 : return 1 
    else: 
        return (fibo1(n - 1) + fibo1(n - 2))

def fibo2(n):
    dp = [0] * 41
    dp[0] = 1
    dp[1] = 1
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n] 
n = int(input())
fib1 = fibo1(n)  
print(fib1, n-2)  
        
    