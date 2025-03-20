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


def find_set(x):   # 부모 노드 탐색 & 경로 압축
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]


def union(x, y):   # 경로 연결 & 사이클 방지
    px = find_set(x)
    py = find_set(y)

    if px != py:
        if px < py:
            p[py] = px
        else:
            p[px] = py
    else:
        return


V, E = map(int, input().split())
edges = []

for _ in range(E):
    start, end, weight = map(int, input().split())
    edges.append((start, end, weight))

edges.sort(key=lambda x: x[2])           # 가중치 기준으로 오름차순 정렬
p = [i for i in range(V)]          # 부모 노드 (make_set)

cnt = 0             # 선택한 간선 개수
result = 0          # 가중치의 합

for u, v, w in edges:

    if find_set(u) != find_set(v):    # u와 v가 연결이 안 되어있다면
        union(u, v)
        cnt += 1
        result += w

        if cnt == V - 1:
            break
