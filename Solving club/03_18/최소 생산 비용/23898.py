# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZVkYpRqDszHBINE&probBoxId=AZVkSAOaDQLHBINE&type=USER&problemBoxTitle=%2803.18%29++%EB%B6%84%ED%95%A0%EC%A0%95%EB%B3%B5+%EB%B0%8F+%EB%B0%B1%ED%8A%B8%EB%9E%98%ED%82%B92&problemBoxCnt=5

import sys
sys.stdin = open("5209_input.txt")


def dfs(mask, row):
    if row == N:        # 모든 행 선택한 경우 덧셈을 위해 0 반환
        return 0

    if dp[mask]:        # 이미 계산한 값 반환
        return dp[mask]

    min_cost = 100*N    # 말도 안되는 큰 값
    for col in range(N):
        if not (mask & (1 << col)):       # 아직 선택 안한 열
            cost = matrix[row][col]
            min_cost = min(min_cost, cost + dfs(mask | (1 << col), row + 1))   # 최솟값 갱신

    dp[mask] = min_cost    # 메모이제이션
    return dp[mask]


T = int(input())
for t in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    dp = [0] * (1 << N)      # dp 배열 초기화
    result = dfs(0, 0)

    print(f"#{t} {result}")
