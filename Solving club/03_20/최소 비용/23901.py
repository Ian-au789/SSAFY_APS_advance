# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZVkaOO6DzLHBINE&probBoxId=AZVkSAOaDQTHBINE&type=USER&problemBoxTitle=%2803.20%29++%EA%B7%B8%EB%9E%98%ED%94%842&problemBoxCnt=5

import sys
sys.stdin = open("5250_input.txt")
import heapq


def dijkstra(start_node):
    pq = [(0, start_node)]
    dists = [MAX] * N**2
    dists[start_node] = 0

    while pq:
        dist, node = heapq.heappop(pq)

        if dists[node] < dist:
            continue

        for next_info in graph[node]:
            next_dist = next_info[0]
            next_node = next_info[1]

            new_dist = next_dist + dist

            if dists[next_node] > new_dist:
                dists[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))

    return dists


T = int(input())
for t in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    graph = [[] for _ in range(N**2)]
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    MAX = 1e9

    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i + d[k][0]
                nj = j + d[k][1]

                if 0 <= ni < N and 0 <= nj < N:
                    slope = matrix[ni][nj] - matrix[i][j]
                    if slope >= 0:
                        graph[N * i + j].append((slope + 1, N * ni + nj))
                    else:
                        graph[N * i + j].append((1, N * ni + nj))

    result = dijkstra(0)
    print(f"#{t} {result[N**2 - 1]}")
