# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AWngfZVa9XwDFAQU&probBoxId=AZVkSAOaDQHHBINE&type=PROBLEM&problemBoxTitle=%2803.17%29++%EB%B6%84%ED%95%A0%EC%A0%95%EB%B3%B5+%EB%B0%8F+%EB%B0%B1%ED%8A%B8%EB%9E%98%ED%82%B91&problemBoxCnt=6

import sys
sys.stdin = open("s_input.txt")


def find_set(x):   # 부모 노드 탐색
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]


def union(x, y):   # 합집합
    px = find_set(x)
    py = find_set(y)

    if px != py:          # 두 노드가 서로 다른 집합에 속해있는 경우
        p[py] = px        # 다른 하나의 부모로 설정하고 랭크 + 1


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    vertex = [list(map(int, input().split())) for _ in range(M)]

    p = [i for i in range(N+1)]

    for v in vertex:
        union(v[0], v[1])

    for i in range(1, N+1):
        find_set(i)

    print(f"#{t} {len(set(p)) - 1}")
