# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV15StKqAQkCFAYD&probBoxId=AZVkSAOaDQTHBINE&type=PROBLEM&problemBoxTitle=%2803.20%29++%EA%B7%B8%EB%9E%98%ED%94%842&problemBoxCnt=5

import sys
sys.stdin = open("input.txt")


def find_set(x):   # 부모 노드 탐색
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    px = find_set(x)
    py = find_set(y)

    if px != py:          # 두 노드가 서로 다른 집합에 속해있는 경우
        if rank[px] > rank[py]:   # y의 랭크가 더 낮으므로 y의 집합을 x의 집합에 합침
            p[py] = px            # y의 집합의 루트 노드의 부모노드로 x의 집합의 루트 노드 설정

        elif rank[px] < rank[py]:
            p[px] = py

        else:                     # 랭크가 동일하면 하나를 다른 하나의 부모로 설정하고 랭크 + 1
            p[py] = px
            rank[px] += 1


T = int(input())
for t in range(1, T+1):
    N = int(input())
    loc_i = list(map(int, input().split()))
    loc_j = list(map(int, input().split()))
    E = float(input())

    edges = []
    for m in range(N):
        for n in range(m+1, N):
            edges.append((m, n, (loc_i[m] - loc_i[n]) ** 2 + (loc_j[m] - loc_j[n]) ** 2))

    edges.sort(key=lambda x: x[2])
    p = [i for i in range(N)]
    rank = [0] * N
    cnt = 0
    dist = 0

    for s, e, w in edges:
        if find_set(s) != find_set(e):
            union(s, e)
            cnt += 1
            dist += w

            if cnt == N - 1:
                break

    print(f"#{t} {round(E * dist)}")
