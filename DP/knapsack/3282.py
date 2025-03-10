# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWBJAVpqrzQDFAWr


import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    items = [list(map(int, input().split())) for _ in range(N)]

    dp = [0] * (K + 1)

    for i in range(N):
        weight, value = items[i]

        for j in range(K, weight - 1, -1):
            dp[j] = max(dp[j], dp[j - weight] + value)    # 해당 물건을 담았을 때와 담지 않았을 때를 비교해서 큰 값만 저장

    print(f"#{t} {dp[K]}")
