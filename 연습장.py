# for t in range(1, T+1):
#     N = int(input())
#     matrix = [list(map(int, input().split())) for _ in range(N)]

from collections import defaultdict

word_count = defaultdict(int)
word_count['apple'] += 1
print(word_count['apple'])  # 출력: 1

list_dict = defaultdict(list)
list_dict['fruits'].append('apple')
list_dict['fruits'].append('banana')
print(list_dict['fruits'])  # 출력: ['apple', 'banana']

set_dict = defaultdict(set)
set_dict['fruits'].add('apple')
set_dict['fruits'].add('banana')
set_dict['fruits'].add('apple')
print(set_dict['fruits'])  # 출력: {'apple', 'banana'}


def floyd_warshall(graph):
    v_len = len(graph)     # 그래프의 정점 수
    dist = [[1e9] * v_len for _ in range(v_len)]       # 거리 행렬

    for i in range(v_len):
        dist[i][i] = 0              # 자기 자신으로의 거리는 0

    for u in range(v_len):
        for v in range(v_len):
            if graph[u][v] != 0:
                dist[u][v] = graph[u][v]    # 인접 행렬사이의 거리로 업데이트

    # 가능한 모든 시작점, 경유 루트, 도착점의 경우를 탐색하면서 최단 경로 갱신
    for k in range(v_len):
        for i in range(v_len):
            for j in range(v_len):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist      # 모든 정점 사이의 최단거리가 반영된 행렬
