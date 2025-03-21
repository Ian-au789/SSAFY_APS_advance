# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZGMC0Lau8sDFAXd&probBoxId=AZVkSAOaDQTHBINE&type=USER&problemBoxTitle=%2803.20%29++%EA%B7%B8%EB%9E%98%ED%94%842&problemBoxCnt=5

import sys
sys.stdin = open("sample_input.txt")
import heapq


def dijkstra():
    pq = [(0, 0)]
    dists = [1e9] * (N+1)
    dists[0] = 0

    while pq:
        dist, node = heapq.heappop(pq)

        if dists[node] < dist:
            continue

        for next_step in graph[node]:
            next_dist = next_step[0]
            next_node = next_step[1]
            new_dist = dist + next_dist

            if dists[next_node] > new_dist:
                dists[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))

    return dists[N]


T = int(input())
for t in range(1, T+1):
    N, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]

    graph = [[] for _ in range(N+1)]
    for s, e, w in edges:
        graph[s].append((w, e))

    print(f"#{t} {dijkstra()}")
