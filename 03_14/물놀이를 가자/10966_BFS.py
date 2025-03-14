# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AXWXMZta-PsDFAST&probBoxId=AZVkSAOaDQDHBINE&type=PROBLEM&problemBoxTitle=%2803.14%29+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B42&problemBoxCnt=4

import sys
sys.stdin = open("sample_input.txt")


def bfs(ci, cj, visited):
    global result
    global N
    global M

    path = [(ci, cj)]
    level = 0
    branch = 1
    next_branch = 0

    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    while path:
        for k in range(4):
            ni = path[0][0] + di[k]
            nj = path[0][1] + dj[k]

            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                if matrix[ni][nj] == "W":
                    return level + 1
                else:
                    path.append((ni, nj))
                    visited[ni][nj] = 1
                    next_branch += 1

        else:
            branch -= 1
            path.pop(0)

            if branch == 0:
                level += 1
                branch = next_branch
                next_branch = 0


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(str, input())) for _ in range(N)]

    land = []
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == "L":
                land.append((i, j))

    result = [0]*len(land)

    for c in range(len(land)):
        v = [[0] * M for _ in range(N)]
        v[land[c][0]][land[c][1]] = 1
        result[c] = bfs(land[c][0], land[c][1], v)

    print(f"#{t} {sum(result)}")
