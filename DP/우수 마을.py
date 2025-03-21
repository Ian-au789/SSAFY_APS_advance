# https://www.acmicpc.net/problem/1949
from collections import defaultdict

def best_village():
    pass


N = 7
population = [1000, 3000, 4000, 1000, 2000, 2000, 7000]
edges = [(1, 2), (2, 3), (4, 3), (4, 5), (6, 2), (6, 7)]
graph = defaultdict(set)
for e in edges:
    graph[e[0]].add(e[1])
    graph[e[1]].add(e[0])

print(graph)
