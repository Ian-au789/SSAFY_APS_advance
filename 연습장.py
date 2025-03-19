from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    board = [[0] * 102 for _ in range(102)]
    visited = [[0] * 102 for _ in range(102)]
    queue = deque()

    # 좌표를 2배 확장하여 사용
    characterX, characterY, itemX, itemY = characterX * 2, characterY * 2, itemX * 2, itemY * 2
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1 * 2, y1 * 2, x2 * 2, y2 * 2
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    board[i][j] = -1     # 내부 영역 (이동 불가능)
                elif board[i][j] != -1:
                    board[i][j] = 1      # 테두리 (이동 가능)

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    queue.append((characterX, characterY, 0))
    visited[characterX][characterY] = 1

    while queue:
        x, y, dist = queue.popleft()

        # 목표 위치 도달
        if (x, y) == (itemX, itemY):
            return dist // 2  # 원래 좌표 기준으로 복원

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if not visited[nx][ny] and board[nx][ny] == 1:
                visited[nx][ny] = 1
                queue.append((nx, ny, dist + 1))


print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))     # 17
print(solution([[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]], 9, 7, 6, 1))     # 11
print(solution([[1, 1, 5, 7]], 1, 1, 4, 7))     # 9
print(solution([[2, 1, 7, 5], [6, 4, 10, 10]], 3, 1, 7, 10))     # 15
print(solution([[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]], 1, 4, 6, 3))     # 10



