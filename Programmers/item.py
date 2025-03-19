# https://school.programmers.co.kr/learn/courses/30/lessons/87694

'''
기존 좌표계에서는 테두리가 사실상 한 넓이를 차지하기 때문에
직사각형이 바로 인접해있거나 가로 세로 길이가 2인 직사각형은 내부 공간과 테두리를 구분하기 어렵다.

그냥 좌표계를 2배로 뻥튀기하면 무조건 공백이 생긴다. 만사 해결
'''

from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    board = [[0] * 102 for _ in range(102)]
    visited = [[0] * 102 for _ in range(102)]
    queue = deque()

    # 좌표계 2배 확장해서  사용
    characterX, characterY, itemX, itemY = characterX * 2, characterY * 2, itemX * 2, itemY * 2
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1 * 2, y1 * 2, x2 * 2, y2 * 2
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    board[i][j] = 2     # 내부 영역 (이동 불가능)
                elif board[i][j] != 2:
                    board[i][j] = 1      # 테두리 (이동 가능)

    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    queue.append((characterX, characterY, 0))
    visited[characterX][characterY] = 1

    while queue:
        ci, cj, dist = queue.popleft()

        # 목표 위치 도달
        if (ci, cj) == (itemX, itemY):
            return dist // 2  # 원래 좌표 기준으로 복원

        for k in range(4):
            ni, nj = ci + di[k], cj + dj[k]

            if not visited[ni][nj] and board[ni][nj] == 1:
                visited[ni][nj] = 1
                queue.append((ni, nj, dist + 1))


print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))     # 17
print(solution([[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]], 9, 7, 6, 1))     # 11
print(solution([[1, 1, 5, 7]], 1, 1, 4, 7))     # 9
print(solution([[2, 1, 7, 5], [6, 4, 10, 10]], 3, 1, 7, 10))     # 15
print(solution([[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]], 1, 4, 6, 3))     # 10

