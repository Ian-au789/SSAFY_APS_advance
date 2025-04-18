
# 벽돌 깨기
def break_brick(ci, cj, number, matrix_bricks):
    global W
    global H
    di = [1, 0, -1, 0]  # 델타 탐색
    dj = [0, 1, 0, -1]
    matrix_bricks[ci][cj] = 0

    for k in range(4):
        for l in range(1, number):  # 상하좌우로 벽돌이 깨지는 범위
            ni = ci + l * di[k]  # 다음에 탐색할 좌표
            nj = cj + l * dj[k]
            if 0 <= ni < W and 0 <= nj < H:
                if matrix_bricks[ni][nj] == 0:  # 벽돌이 없는 빈 공간은 스킵
                    continue
                elif matrix_bricks[ni][nj] == 1:  # 벽돌 번호가 1인 경우 부수기
                    matrix_bricks[ni][nj] = 0
                else:  # 벽돌 번호가 2 이상인 경우 해당 연쇄 작용 탐색 (재귀호출)
                    break_brick(ni, nj, matrix_bricks[ni][nj], matrix_bricks)
    return


# 구슬 쏘기 및 남은 벽돌 세기
def bricks_left(number, bricks):
    global W
    global H
    global result
    check = 0

    if number == 0:  # 구슬을 모두 쐈다면 남아있는 벽돌의 수 세서 최소값 갱신
        cnt = 0
        for i in range(W):
            for j in range(H):
                if bricks[i][j] > 0:
                    cnt += 1
        if result > cnt:
            result = cnt

    else:
        for i in range(W):  # 모든 행에서 구슬 한 번씩 쏘기
            idx = 0
            while bricks[i][idx] == 0:  # 맨 위의 벽돌 찾기
                idx += 1
                if idx == H:
                    break

            if idx == H:  # 해당 행에 벽돌이 없으면 다음 행 탐색
                check += 1
                continue

            else:
                new_bricks = [row[:] for row in bricks]
                break_brick(i, idx, new_bricks[i][idx], new_bricks)  # 벽돌에 부딪히면 벽돌 깨기

                # 스택을 써서 남은 벽돌을 아래로 떨어뜨리기
                for row in new_bricks:
                    stack = []
                    for j in range(H):
                        if row[j] > 0:
                            stack.append(row[j])
                    top = H - 1
                    while top >= 0:
                        if len(stack) > 0:
                            row[top] = stack.pop()
                        else:
                            row[top] = 0
                        top -= 1

                bricks_left(number - 1, new_bricks)  # 다음 구슬 쏘기

        if check == W:  # 만약 모든 행에 구슬이 없으면 모든 벽돌 깨기 완료
            result = 0
            return


T = int(input())
for t in range(1, T + 1):
    N, W, H = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(H)]
    matrix_t = list(map(list, zip(*matrix)))  # 남아있는 벽돌을 떨어뜨릴 때 행과 열을 바꾸면 더 편함
    result = W * H
    bricks_left(N, matrix_t)

    print(f"#{t} {result}")