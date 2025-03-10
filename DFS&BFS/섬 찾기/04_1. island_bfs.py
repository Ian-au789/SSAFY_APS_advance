import sys
from collections import deque
sys.stdin = open('island_input.txt')


def find_island(island, x, y):
    # 상, 하, 좌, 우, 대각선 방향 모두 정의 (8방향)
    dxy = [(-1, 0), (1,0), (0, -1), (0, 1), (-1, -1), (1, -1), (1, 1), (-1, 1)]
    queue = deque([(x, y)])
    island[x][y] = 0

    while queue:
        cx, cy = queue.popleft()

        for dx, dy in dxy:
            nx, ny = cx + dx, cy + dy

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 이미 방문한 경우 or 바다인 경우 ( 방문한 경우 => 바다로 바꿈 )
            if island[nx][ny] == 0:
                continue
            # 다음 땅으로 이동할 수 있음
            queue.append((nx, ny))
            island[nx][ny] = 0

n, m = map(int, input().split())  # 섬의 크기 입력
arr = [list(map(int, input())) for _ in range(n)]  # 섬의 상태 입력 받기
island_cnt = 0  # 섬의 개수

# 그래프이고, 모든 vertex가 서로 인접해있다는 보장이 없다!
# 모든 정점에서 bfs를 실행해야 한다.
for i in range(n):
    for j in range(m):
        # 바다에서 시작하며 안되니까 -> 땅인 곳에서 bfs 탐색 시작
        # find_island 함수에서 이미 탐색한 곳은 0으로 변경
        # 이미 탐색한 곳을 BFS 탐색을 할 필요 없음 
        if arr[i][j] == 1:
            # BFS 함수에서 탐색한 땅을 0으로 변경할 거기 떄문에 arr를 건네주자
            # 사실 안건네주고 global 을 사용해도 괜찮다
            find_island(arr, i, j)  # BFS 탐색 시작
            island_cnt += 1  # BFs 탐색을 완료하면 섬의 개수를 증가

print(island_cnt)  # 섬의 개수 출력
