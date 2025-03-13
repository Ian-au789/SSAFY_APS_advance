# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZVkVDT6DfzHBINE&probBoxId=AZVkSAOaDP7HBINE&type=USER&problemBoxTitle=%2803.12%29+%EC%99%84%EC%A0%84%ED%83%90%EC%83%89+%EB%B0%8F+%EA%B7%B8%EB%A6%AC%EB%94%941&problemBoxCnt=5

import sys
sys.stdin = open("5188_input.txt")


def minimum_path(ci, cj, size, path):
    global result

    if ci == size - 1 and cj == size - 1:
        path += matrix[ci][cj]
        if path < result:                # 최솟값 갱신
            result = path
        return

    if path >= result:                   # 백트래킹
        return

    if ci + 1 < N:
        minimum_path(ci + 1, cj, size, path + matrix[ci][cj])     # 아래로 이동

    if cj + 1 < N:
        minimum_path(ci, cj + 1, size, path + matrix[ci][cj])     # 오른쪽으로 이동


T = int(input())
for t in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = sum([sum(row) for row in matrix])

    minimum_path(0, 0, N, 0)

    print(f"#{t} {result}")
