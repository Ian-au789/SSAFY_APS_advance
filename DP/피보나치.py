# 피보나치를 동적계획법으로 풀이

def fibo_dp(n):
    if n <= 1:
        return n

    dp = [0] * n
    dp[1] = 1
    dp[0] = 1

    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n-1]


print(fibo_dp(10))
