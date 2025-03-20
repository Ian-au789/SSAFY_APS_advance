# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZGMAyt6u7ADFAXd&probBoxId=AZVkSAOaDQTHBINE&type=USER&problemBoxTitle=%2803.20%29++%EA%B7%B8%EB%9E%98%ED%94%842&problemBoxCnt=5

import sys
sys.stdin = open("sample_input.txt")
import heapq


def prim():
    pq = [(0, 0)]
    mst = [0]*V
    route = 0

    while pq:
        weight, node = heapq.heappop(pq)      # heapq가 가장 가중치가 작은 노드를 반환

        if mst[node]:     # 방문한적 있는 노드 제외
            continue

        mst[node] = 1
        route += weight

        for next_node in range(V):
            if graph[node][next_node] and not mst[next_node]:
                heapq.heappush(pq, (graph[node][next_node], next_node))

    return route


T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    V += 1
    graph = [[0]*V for _ in range(V)]

    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s][e] = w                 # 무방향 그래프
        graph[e][s] = w

    print(f"#{t} {prim()}")
