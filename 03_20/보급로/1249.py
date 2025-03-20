# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV15QRX6APsCFAYD&probBoxId=AZVkSAOaDQTHBINE&type=PROBLEM&problemBoxTitle=%2803.20%29++%EA%B7%B8%EB%9E%98%ED%94%842&problemBoxCnt=5

import sys
sys.stdin = open("input.txt")
import heapq


def dijkstra():
    pq = [(0, 0, 0)]
    dists = [[1e9] * N for _ in range(N)]
    dists[0][0] = 0  # 시작점 거리 0
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while pq:
        dist, ci, cj = heapq.heappop(pq)

        if dist > dists[ci][cj]:
            continue

        for di, dj in directions:
            ni, nj = ci + di, cj + dj

            if 0 <= ni < N and 0 <= nj < N:
                cost = matrix[ni][nj]
                new_dist = dist + cost

                if dists[ni][nj] > new_dist:
                    dists[ni][nj] = new_dist
                    heapq.heappush(pq, (new_dist, ni, nj))

    return dists[N-1][N-1]


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]

    result = dijkstra()
    print(f"#{t} {result}")
