# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV15QRX6APsCFAYD&probBoxId=AZVkSAOaDQTHBINE&type=PROBLEM&problemBoxTitle=%2803.20%29++%EA%B7%B8%EB%9E%98%ED%94%842&problemBoxCnt=5

import sys
sys.stdin = open("input.txt")


def dfs(cur_loc, goal, time):
    global result

    time += matrix[cur_loc[0]][cur_loc[1]]

    if cur_loc == goal:
        result = min(result, time)

    if time >= result:
        return

    for k in range(2):
        next_loc = (cur_loc[0] + di[k], cur_loc[1] + dj[k])

        if 0 <= next_loc[0] < N and 0 <= next_loc[1] < N:
            dfs(next_loc, goal, time)


T = int(input())
for t in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]

    di = [1, 0]
    dj = [0, 1]
    result = 1e9

    dfs((0, 0), (N-1, N-1), 0)
    print(f"#{t} {result}")
