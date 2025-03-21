# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZIyCYJ6p30DFAQP&probBoxId=AZVkSAOaDQXHBINE&type=USER&problemBoxTitle=%2803.21%29++%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B43&problemBoxCnt=6

import sys
sys.stdin = open("sample_input.txt")


def dfs(ci, cj, direction, cnt, log):
    global result

    if matrix[ci][cj] == 3:
        result = min(result, cnt)
        return

    if cnt >= result:
        return

    for k in range(4):
        ni = ci + di[k]
        nj = cj + dj[k]

        if 0 <= ni < N and 0 <= nj < N:  # 범위 내로 이동
            if visited[ni][nj]:          # 이미 지나간 칸 재방문 방지
                continue

            if k == direction:              # 방향이 그대로면 조작 1번
                new_cnt = cnt + 1
            elif k == (direction + 2) % 4:  # 반대 방향으로 이동하면 조작 3번
                new_cnt = cnt + 3
            else:                           # 그 외에는 조작 2번
                new_cnt = cnt + 2

            if matrix[ni][nj] == 1:      # 다음 이동 칸에 나무가 있는 경우
                if log == 0:             # 나무 베는 횟수를 다 썼으면 진행 불가
                    continue
                else:
                    visited[ni][nj] = 1
                    dfs(ni, nj, k, new_cnt, log - 1)
                    visited[ni][nj] = 0
            else:
                visited[ni][nj] = 1
                dfs(ni, nj, k, new_cnt, log)
                visited[ni][nj] = 0


T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    matrix = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        string = input()
        for j in range(N):
            if string[j] == "G":
                continue
            elif string[j] == "T":
                matrix[i][j] = 1
            elif string[j] == "X":
                matrix[i][j] = 2
                start = (i, j)
                visited[i][j] = 1
            else:
                matrix[i][j] = 3

    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]
    result = 1e9
    dfs(start[0], start[1], 2, 0, K)

    if result == 1e9:       # 목적지까지 못 도달했으면 -1
        result = -1

    print(f"#{t} {result}")
