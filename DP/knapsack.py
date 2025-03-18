def knapsack(weights, values, W):
    N = len(weights)
    dp = [[0] * (W + 1) for _ in range(N + 1)]  # DP 테이블 초기화

    for i in range(1, N + 1):  # 물건 개수만큼 반복
        for w in range(W + 1):  # 무게 제한까지 반복
            if weights[i - 1] <= w:
                # 물건을 포함하거나 포함하지 않는 경우 중 최댓값
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]  # 물건을 포함할 수 없는 경우

    print(dp)
    return dp[N][W]  # 최적해 반환

# 예제 실행
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
W = 5
print(knapsack(weights, values, W))  # 출력: 7

