def tsp(N, cost):
    dp = [[float('inf')] * N for _ in range(1 << N)]
    dp[1][0] = 0  # 0번 도시에서 출발

    for mask in range(1 << N):
        for i in range(N):  # 마지막 도시 i
            if dp[mask][i] == float('inf'):
                continue
            for j in range(N):  # 도시 j로 이동
                if not (mask & (1 << j)):  # 아직 방문하지 않은 도시 j
                    dp[mask | (1 << j)][j] = min(dp[mask | (1 << j)][j], dp[mask][i] + cost[i][j])

    return min(dp[(1 << N) - 1][i] + cost[i][0] for i in range(1, N))

# 예시
N = 4
cost = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

print(tsp(N, cost))  # 최단 경로 출력
