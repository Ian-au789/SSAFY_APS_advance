# https://school.programmers.co.kr/learn/courses/30/lessons/87694

'''
1. 좌표가 소속된 사각형의 루트를 따라 이동함
2. 만약 사각형끼리 중첩되는 지점에 도착하면 방향을 수직으로 전환, 이때 다음 선택지가 1인 경우을 선택
'''


def solution(rectangle, characterX, characterY, itemX, itemY):
    cnt = 0

    # matrix 크기 정하기
    bound_i = []
    bound_j = []
    for rect in rectangle:
        bound_i.append(rect[2])
        bound_j.append(rect[3])

    matrix = [[0] * (max(bound_j) + 2) for _ in range(max(bound_i) + 2)]

    # 직사각형 색칠하기 (테두리는 1, 내부는 2)
    idx = 1
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



    for rect in rectangle:
        for i in range(rect[0] + 1, rect[2]):
            for j in range(rect[1] + 1, rect[3]):
                matrix[i][j] = 2

    print(matrix)
    origin = [characterX, characterY]
    cur_loc = [characterX, characterY]
    item_loc = [itemX, itemY]

    return cnt


print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))     # 17
print(solution([[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]], 9, 7, 6, 1))     # 11
print(solution([[1, 1, 5, 7]], 1, 1, 4, 7))     # 9
print(solution([[2, 1, 7, 5], [6, 4, 10, 10]], 3, 1, 7, 10))     # 15
print(solution([[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]], 1, 4, 6, 3))     # 10
