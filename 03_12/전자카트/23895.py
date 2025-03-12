# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZVkVajKDhjHBINE&probBoxId=AZVkSAOaDP7HBINE&type=USER&problemBoxTitle=%2803.12%29+%EC%99%84%EC%A0%84%ED%83%90%EC%83%89+%EB%B0%8F+%EA%B7%B8%EB%A6%AC%EB%94%941&problemBoxCnt=5

import sys
sys.stdin = open("input.txt")


def minimum_battery(area, size, battery):
    global result

    if area == 0:
        if battery < result:
            result = battery
        return

    if battery > result:
        return

    for n in range(1, size):
        if not visited[n]:
            visited[n] = 1
            minimum_battery(n, size, battery + matrix[area][n])
            visited[n] = 0
    else:
        if sum(visited) == size - 1:
            minimum_battery(0, size, battery + matrix[area][0])


T = int(input())
for t in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    result = sum([sum(row) for row in matrix])

    visited = [0] * N

    for i in range(1, N):
        visited[i] = 1
        minimum_battery(i, N, matrix[0][i])
        visited[i] = 0

    print(f"#{t} {result}")
