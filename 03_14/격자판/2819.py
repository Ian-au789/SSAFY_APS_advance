# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7I5fgqEogDFAXB

import sys
sys.stdin = open("sample_input.txt")


def dfs(ci, cj, level, num):

    if level == 7:
        pos_num.add(num)
        return

    for k in range(4):
        ni = ci + di[k]
        nj = cj + dj[k]

        if 0 <= ni < 4 and 0 <= nj < 4:
            dfs(ni, nj, level + 1, num + 10 ** level * matrix[ni][nj])


T = int(input())
for t in range(1, T+1):
    matrix = [list(map(int, input().split())) for _ in range(4)]

    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    pos_num = set()

    for i in range(4):
        for j in range(4):
            dfs(i, j, 1, matrix[i][j])

    print(f"#{t} {len(pos_num)}")
