# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV5LtJYKDzsDFAXc&probBoxId=AZVkSAOaDP7HBINE&type=PROBLEM&problemBoxTitle=%2803.12%29+%EC%99%84%EC%A0%84%ED%83%90%EC%83%89+%EB%B0%8F+%EA%B7%B8%EB%A6%AC%EB%94%941&problemBoxCnt=5

import sys
sys.stdin = open("input.txt")


def next_door(ci, cj, size, path, num):
    global room_num
    global max_path
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]
    move = 1

    while move == 1:          # DFS 쓰면 maximum depth recursion 발생할 수 밖에 없는 testcase 존재
        for k in range(4):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0 <= ni < size and 0 <= nj < size and matrix[ni][nj] == matrix[ci][cj] + 1:
                move = 1
                ci = ni
                cj = nj
                path += 1
                break
        else:
            move = 0

    return num, path


T = int(input())
for t in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    room_num = N ** 2
    max_path = 0

    for i in range(N):
        for j in range(N):
            num, path = next_door(i, j, N, 1, matrix[i][j])

            if max_path < path:          # 최댓값 갱신
                max_path = path
                room_num = num

            elif max_path == path:       # 경로 크기가 같으면 방 번호 작은 걸로
                if num < room_num:
                    room_num = num

    print(f"#{t} {room_num} {max_path}")
