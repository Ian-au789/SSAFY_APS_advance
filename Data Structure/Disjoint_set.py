# 서로소 집합의 연산을 구현해보자

N = 10
p = [0] * (N + 1)
rank = [0] * (N + 1)


def make_set(x):   # 각 노드가 자기 자신을 부모로 가지도록 초기화
    p[x] = x


def find_set(x):   # 부모 노드 탐색
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    px = find_set(x)
    py = find_set(y)

    if px != py:          # 두 노드가 서로 다른 집합에 속해있는 경우
        if rank[px] > rank[py]:   # y의 랭크가 더 낮으므로 y의 집합을 x의 집합에 합침
            p[py] = px            # y의 집합의 루트 노드의 부모노드로 x의 집합의 루트 노드 설정

        elif rank[px] < rank[py]:
            p[px] = py

        else:                     # 랭크가 동일하면 하나를 다른 하나의 부모로 설정하고 랭크 + 1
            p[py] = px
            rank[px] += 1


for i in range(1, N+1):
    make_set(i)

union(1, 2)
union(2, 3)

print(p)
print(rank)
