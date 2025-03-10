# x,y: 현재 좌표
# count: 여태까지 움직인 횟수
def dfs(x, y, count):
    global min_count

    # 종료조건부터 작성을 해보죠
    if x == N - 1 and y == M - 1:
        min_count = min(min_count, count)
        return

    # 하, 우, 상, 좌 (순서는 자율적으로, 저는 예시를 위해서 적합한거에요)
    dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy

        # 제 스타일대로 작성해볼게요
        # 범위를 벗어난 경우
        if nx < 0 or nx >= N or ny < 0 or ny >= M: continue

        # 방문한 적이 있으면 skip
        if visited[nx][ny]: continue

        # 길이 아니면 skip
        if not road[nx][ny]: continue

        # 본인 방문 체크하고, 자기 자신에 다음 좌표와 이동 거리 + 1을 넘김
        visited[nx][ny] = True
        dfs(nx, ny, count + 1)
        # 이렇게 하면 끝인가요 ?
        # DFS가 결국 마지막 갈 곳이 없는 곳까지 간 다음에는 되돌아오잖아요
        visited[nx][ny] = False


# 입력 받기
N, M = map(int, input().split())
road = [list(map(int, input())) for _ in range(N)]

# 방문 여부를 확인하기 위한 변수
visited = [[False] * M for _ in range(N)]
# 최소 이동 횟수를 저장할 변수
# 이게 싫으면 N * M 으로 놔도 된다.
# 왜냐면 많이 움직여봤자 N*M 이니까
min_count = float('inf')
# 0,0 에서 시작
visited[0][0] = True
# 일반적으로 파라미터에 뭘 넘기냐 ?
# 1. 종료 조건이 될 수 있는 변수 ( 이동 좌표 -> 목적지에 도착하면 dfs 중단)
# 2. 결국 얻으려는 누적값 (글로벌 체크할 수도 있다.) ( 여태까지 움직인 횟수 )
dfs(0, 0, 0)
