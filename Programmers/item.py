# https://school.programmers.co.kr/learn/courses/30/lessons/87694

'''
BFS 활용
1. 내 현재 좌표가 어떤 사각형의 테두리 위에 있는지 확인.
2. 델타 탐색을 통해 해당 사각형의 테두리 중에 이동 가능한 경우로 이동
3. 만약 해당 좌표값이 2 (사각형 내부의 값) 이 되거나 양옆이 2라면 제거
'''

from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    cnt = 0
    size = len(rectangle)

    # matrix 크기 정하기
    bound_i = []
    bound_j = []
    for rect in rectangle:
        bound_i.append(rect[2])
        bound_j.append(rect[3])

    matrix = [[0] * (max(bound_j) + 2) for _ in range(max(bound_i) + 2)]

    # 직사각형 색칠하기 (테두리는 1, 내부는 2)
    outlines = []
    for rect in rectangle:
        route = set()
        for i in [rect[0], rect[2]]:
            for j in range(rect[1], rect[3] + 1):
                matrix[i][j] = 1
                route.add((i, j))

        for j in [rect[1], rect[3]]:
            for i in range(rect[0], rect[2] + 1):
                matrix[i][j] = 1
                route.add((i, j))

        outlines.append(route)             # 각 직사각형의 테두리 집합으로 저장

    for rect in rectangle:
        for i in range(rect[0] + 1, rect[2]):
            for j in range(rect[1] + 1, rect[3]):
                matrix[i][j] = 2

    # BFS 탐색 시작
    item = (itemX, itemY)
    queue = deque((characterX, characterY))

    while queue[0] != item:
        cur_loc = queue[0]

        for i in range(size):
            if cur_loc in outlines[i]:
                for k in range(4):
                    next_loc = (cur_loc[0] + di[k], cur_loc[1] + dj[k])

                    if next_loc in outlines[i] and matrix[next_loc[0]][next_loc[1]] == 1:




    return cnt


print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))     # 17
print(solution([[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]], 9, 7, 6, 1))     # 11
print(solution([[1, 1, 5, 7]], 1, 1, 4, 7))     # 9
print(solution([[2, 1, 7, 5], [6, 4, 10, 10]], 3, 1, 7, 10))     # 15
print(solution([[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]], 1, 4, 6, 3))     # 10
