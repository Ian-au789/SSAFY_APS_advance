import sys
sys.stdin = open("5250_input.txt")
import heapq


def dijkstra():
    pq = [(0, 0, 0)]
    dists = [[MAX] * N for _ in range(N)]
    dists[0][0] = 0  # 시작점 거리 0
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while pq:
        dist, x, y = heapq.heappop(pq)

        if dist > dists[x][y]:
            continue

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N:
                # 가중치 계산 (오르막이면 추가 비용, 내리막은 1)
                slope = matrix[nx][ny] - matrix[x][y]
                if slope > 0:
                    new_dist = dist + slope + 1
                else:
                    new_dist = dist + 1

                if dists[nx][ny] > new_dist:
                    dists[nx][ny] = new_dist
                    heapq.heappush(pq, (new_dist, nx, ny))

    return dists[N-1][N-1]


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    MAX = int(1e9)

    result = dijkstra()
    print(f"#{t} {result}")
