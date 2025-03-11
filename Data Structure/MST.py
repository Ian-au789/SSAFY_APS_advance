# 최소 신장 트리를 찾는 두 방법을 알아보자

class DisjointSet:
    def __init__(self, v):
        self.p = [0] * (len(v) + 1)        # 서로소 집합 준비

    def make_set(self, x):
        self.p[x] = x

    def find_set(self, x):                 # 루트 노드 찾기
        if x != self.p[x]:
            self.p[x] = self.find_set(self.p[x])   # 경로 압축

        return self.p[x]

    def union(self, x, y):                 # 합집합 (루트 노드 동일하게)
        px = self.find_set(x)
        py = self.find_set(y)

        if px < py:
            self.p[py] = px
        else:
            self.p[px] = py


def mst_kruskal(vertices, edges):
    mst = []
    n = len(vertices)
    ds = DisjointSet(vertices)

    for i in range(n+1):
        ds.make_set(i)

    edges.sort(key=lambda x: x[2])          # 가중치 기준으로 오름차순 정렬

    for edge in edges:
        s, e, w = edge

        if ds.find_set(s) != ds.find_set(e):    # 루트노드가 동일하다면 사이클이 생성됨
            ds.union(s, e)                      # 간선으로 연결되었으니 합집합
            mst.append(edge)                    # 해당 간선 최소 신장 트리에 저장

    return mst


edge_list = [[1, 2, 1], [2, 3, 3], [1, 3, 2]]
vertex_list = [1, 2, 3]

print(mst_kruskal(vertex_list, edge_list))
