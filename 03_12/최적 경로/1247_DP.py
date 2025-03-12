# https://swexpertacademy.com/main/talk/solvingClub/problemBoxDetail.do?solveclubId=AZTP1QzqXnbHBIRD&probBoxId=AZVkSAOaDP7HBINE

import sys
sys.stdin = open("input.txt")


def tsp(size, dist):
    dp = [[float('inf')] * size for _ in range(1 << size)]
    dp[1][0] = 0

    for mask in range(1, 1 << size):
        for i in range(size):
            if dp[mask][i] == float('inf'):
                continue

            for j in range(size):
                if not (mask & (1 << j)):
                    dp[mask | (1 << j)][j] = min((dp[mask][i] + dist[i][j]), dp[mask | (1 << j)][j])

    return min([dp[(1 << size) - 1][k] + dist[size][k] for k in range(1, size)])


T = int(input())
for t in range(1, T+1):
    N = int(input())
    cor = list(map(int, input().split()))
    loc = [[cor[2*i], cor[2*i+1]] for i in range(N + 2) if i != 1]
    loc.append([cor[2], cor[3]])   # 회사 : 0, 고객 : 1~N, 집 : N+1

    distances = [[abs(loc[j][0] - loc[i][0]) + abs(loc[j][1] - loc[i][1]) for j in range(N+1)] for i in range(N+2)]

    print(f"#{t} {tsp(N + 1, distances)}")
