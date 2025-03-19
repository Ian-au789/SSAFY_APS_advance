# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZGL6M0Ku1wDFAXd&probBoxId=AZVkSAOaDQPHBINE&type=USER&problemBoxTitle=%2803.19%29++%EA%B7%B8%EB%9E%98%ED%94%841&problemBoxCnt=3

import sys
sys.stdin = open("sample_input.txt")


def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    px = find_set(x)
    py = find_set(y)

    if px != py:
        p[py] = px


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    input_list = list(map(int, input().split()))

    numbers = list(range(1, N+1))
    p = list(range(N+1))
    team = []
    for i in range(M):
        team.append((input_list[2*i], input_list[2*i+1]))

    for te in team:
        union(te[0], te[1])

    roots = set()
    for i in range(N+1):
        roots.add(find_set(i))

    print(f"#{t} {len(roots) - 1}")
