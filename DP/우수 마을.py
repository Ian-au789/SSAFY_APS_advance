# https://www.acmicpc.net/problem/1949

# 트리에서 DP를 다루는 방법을 알아야 함, 특정 노드를 부모노드로 가지는 자식 노드의 값을 업데이트하는 형식

from collections import defaultdict

def best_village(num):
    for next_num in graph[num]:
        if visited[next_num-1]:
            continue


N = 7
population = [1000, 3000, 4000, 1000, 2000, 2000, 7000]
edges = [(1, 2), (2, 3), (4, 3), (4, 5), (6, 2), (6, 7)]
graph = defaultdict(set)
for e in edges:
    graph[e[0]].add(e[1])
    graph[e[1]].add(e[0])

visited = [0]*N

result = best_village(1)

print(graph)
