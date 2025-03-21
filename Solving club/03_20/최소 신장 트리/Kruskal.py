# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZGMAyt6u7ADFAXd&probBoxId=AZVkSAOaDQTHBINE&type=USER&problemBoxTitle=%2803.20%29++%EA%B7%B8%EB%9E%98%ED%94%842&problemBoxCnt=5

import sys
sys.stdin = open("sample_input.txt")


def find_set(x):   # 부모 노드 탐색 & 경로 압축
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]


def union(x, y):   # 경로 연결 & 사이클 방지
    px = find_set(x)
    py = find_set(y)

    if px != py:
        if px < py:
            p[py] = px
        else:
            p[px] = py
    else:
        return


T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    edges = []

    for _ in range(E):
        s, e, w = map(int, input().split())
        edges.append((s, e, w))

    edges.sort(key=lambda x: x[2])        # Kruskal 방식
    p = [i for i in range(V + 1)]

    cnt = 0
    weights = 0

    for s, e, w in edges:
        if find_set(s) != find_set(e):
            union(s, e)
            cnt += 1
            weights += w

            if cnt == V:
                break

    print(f"#{t} {weights}")
