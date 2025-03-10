import sys
from collections import deque
sys.stdin = open('practice_input.txt')

# 기존에는 큐에 다음에 방문할 정점을 집어넣잖아요
# 이번에는 방문할 정점 + 여태까지 이동한 횟수를 같이 넣어줄거에요
# 사실 이렇게 풀어도 어차피 방문 여부를 확인하는 변수는 있어야 해요.
# 큐에 정점을 집어넣을 때, 같이 부가 데이터를 넣어야하는 경우가 있어요..
# "이런식으로 풀 수 있다"에 집중
def get_road_move_time(road, n, m):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # 그래도 결국 방문 여부를 확인하는 변수가 필요하다.
    visited = [[False] * m for _ in range(n)]

    # 처음 시작 노드를 queue 에 집어 넣어 준다.
    # 원래는 시작 좌표만 집어넣었는데, 이제 현재까지 이동한 거리도 넣어준다.
    queue = deque([(0, 0, 0)])

    while queue:
        # x좌표, y좌표, 현재좌표까지의 이동 거리
        x, y, dist = queue.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            # 아까는 다음 좌표만 구했지만,
            # 다음 좌표까지의 이동거리도 구해야 한다.
            next_dist = dist + 1

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and road[nx][ny] == 1:
                queue.append((nx, ny, next_dist))

                if nx == n-1 and ny == m-1:
                    return next_dist
    return -1

# 도로의 크기 n * m 입력 받기
n, m = map(int, input().split())
road = [list(map(int, input())) for _ in range(n)]  # 도로 정보 입력

result = get_road_move_time(road, n, m)  # BFS를 이용해서 이동시간 구하기
print(result)
