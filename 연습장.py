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


import heapq


def dijkstra(start_node):
    pq = [(0, start_node)]
    dists = [MAX] * V
    dists[start_node] = 0

    while pq:
        dist, node = heapq.heappop(pq)

        if dists[node] < dist:      # 이미 더 작은 경로가 존재한다면 pass
            continue

        for next_info in graph[node]:
            next_dist = next_info[0]
            next_node = next_info[1]

            new_dist = dist + next_dist

            if dists[next_node] <= new_dist:
                continue
            else:
                dists[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))


MAX = 1e9

V, E = map(int, input().split())
start_node = 0
graph = [[] for _ in range(V)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))           # 단방향 그래프
