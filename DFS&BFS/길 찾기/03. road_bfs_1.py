import sys
from collections import deque
sys.stdin = open('practice_input.txt')

# 1. 전체 공간을 복사해서 각 공간의 좌표마다 시작지점에서 얼마나
# 이동했는 지를 저장하는 방식으로 구현~
# 장점: 모든 목적지의 최단 거리를 알 수 있다. (시작지점 (0,0) 에 출발한다는 조건하에)
# 단점: 메모리를 2배로 차지한다.
def get_road_move_time(road, n, m):
    # 하, 우, 상, 좌
    # dxy를 for loop로 돌면서 현재 좌표에 dxy를 더해주면, 상하좌우로 이동할 수 있다.
    dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    # 문제에서는 [1, 1]에서 시작해서 [N, M]에 도착해야 하지만
    # 우리가 입력을 2차원 배열로 받아서 [1,1] -> [0,0] 맵핑이 됐죠.
    # 우리는 결국 [0,0] -> [N-1][M-1]에 도달하는 경로를 찾으면 된다.
    queue = deque([(0, 0)])

    # 복사하고, 각 좌표까지 걸리는 최단 이동 거리를 저장하자
    # 노드가 한 번 방문한 적이 있는 지 확인하는 용도로도 사용이 된다.
    # 여기는 사실 꼭 -1이 아니여도 된다.
    # '-', 0 이든 자유롭게 문제의 조건을 잘 피할 수 있도록 자유롭게 작성
    distance = [[-1] * m for _ in range(n)]
    distance[0][0] = 0  # 처음 시작 부분은 0으로 시작

    # 큐가 빌 때까지 큐에 있는 것을 꺼내서 반복적으로 최단 거리를 저장
    while queue:
        x, y = queue.popleft()  # 현재 위치

        for dx, dy in dxy:  # 순회하면서 아래, 오른쪽, 위 , 왼쪽을 순서대로 이동시킨다.
            nx, ny = x + dx, y + dy  # 현재 위치에서 각 방향으로 이동

            # 1. 도로 범위 안에 포함될 것
            # 2. 방문한 적이 없을 것 ( 가야할 곳이 (-1) 이여야 한다.)
            # 3. 갈 수있는 곳 ( 길일 것 !)
            if 0 <= nx < n and 0 <= ny < m and distance[nx][ny] == -1 and road[nx][ny] == 1:
                # 조건을 통과했으니 이제 이동하자.!!
                queue.append((nx, ny))
                # 현재 위치까지 오는데 걸린 이동 횟수 + 1 값을
                # 다음에 이동해야 할 좌표에 입력을 한다.
                distance[nx][ny] = distance[x][y] + 1

                if nx == n-1 and ny == m-1:
                    return distance[nx][ny]

    # 문제에서 목적지에 도착하지 못하면 "어떤 값"을 출력하세요 ~ 이런식으로 출제가 됩니다.
    return -1  # 문제에서 요구하는 값을 넣으면 된다.

# 도로의 크기 n * m 입력 받기
n, m = map(int, input().split())
# 도로 정보 입력
road = [list(map(int, input())) for _ in range(n)]

# BFS를 이용해서 이동시간 구하기
result = get_road_move_time(road, n, m)
print(result)
