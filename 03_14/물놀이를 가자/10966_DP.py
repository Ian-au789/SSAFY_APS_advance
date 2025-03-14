
import sys
sys.stdin = open("sample_input.txt")


# BFS로는 실행시간이 버티질 못해서 dp로 풀어봤다.
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(str, input())) for _ in range(N)]

    dp = [[N*M] * M for _ in range(N)]         # 절대 도달할 수 없는 큰 수
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == "W":            # 물이 있는 구역에서는 거리가 0
                dp[i][j] = 0

    # 왼쪽에서 오른쪽, 오른쪽에서 왼쪽으로 거리 갱신
    for row in dp:
        for k in range(1, M):
            row[k] = min(row[k], row[k-1] + 1)
            row[M - k - 1] = min(row[M - k - 1], row[M - k] + 1)

    # 위에서 아래, 아래에서 위로 거리 갱신
    for m in range(M):
        for n in range(1, N):
            dp[n][m] = min(dp[n][m], dp[n - 1][m] + 1)
            dp[N - n - 1][m] = min(dp[N - n - 1][m], dp[N - n][m] + 1)

    result = 0
    # 총합 구하기
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == "L":
                result += dp[i][j]

    print(f"#{t} {result}")
