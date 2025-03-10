import sys

sys.stdin = open('island_input.txt')


# BFS 와 DFS의 시간복잡도는 동일하다.
# 두 알고리즘 모두 모든 땅을 한 번씩만 방문하기 때문에 O(n*m)의 시간복잡도
# 근데 이 문제는 사실 DFS로 푸는 게 더 코드가 간단

# 단점은 스택이 조금 깊어서, 오버플로우가 날 수도 있겠다!
def dfs(x, y):
    dxy = [(-1, 0), (1,0), (0, -1), (0, 1), (-1, -1), (-1, 1),(1, -1), (1,1)]
    island[x][y] = 0  # 방문한 땅을 0으로 바꾼다

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy

        # 범위를 벗어난 곳
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        # 방문할 수 없는 곳
        if not island[nx][ny]:
            continue

        dfs(nx, ny)

n, m = map(int, input().split())  # 섬의 크기 입력
island = [list(map(int, input())) for _ in range(n)]  # 섬의 상태 입력 받기
island_cnt = 0  # 섬의 개수

for i in range(n):
    for j in range(m):
        if island[i][j] == 1:
            # (일반적으로) 종료 조건, 누적해서 가지고 있는 결과값
            dfs(i, j)
            island_cnt += 1

print(island_cnt)  # 섬의 개수 출력
