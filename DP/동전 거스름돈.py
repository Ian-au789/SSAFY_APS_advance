# 해당 가격을 제일 적은 거스름돈을 나눠줄 수 있는 방법 동적계획법으로 탐색

def coin_change(price):
    coin = [1, 5, 10, 50]

    dp = [price] * (price + 1)
    dp[0] = 0

    for i in range(1, price + 1):
        for c in coin:
            if price >= c:
                dp[i] = min(dp[i], dp[i - c] + 1)

    return dp[price]


print(coin_change(108))
