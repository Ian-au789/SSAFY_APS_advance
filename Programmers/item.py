# https://school.programmers.co.kr/learn/courses/30/lessons/87694

'''
1. BFS를 써서 목표 지점까지 최단경로 확인
2. 델타 탐색으로 다음 좌표가 사각형의 테두리에서만 움직이도록 함
3. 해당 좌표가 속하는 사각형 테두리는 전부 탐색
4. 만약 상자 내부에 들어가거나, 직사각형 한 변의 길이가 2라서 관통하지 않도록 제한
'''

from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    queue = deque()
    queue.append([(characterX, characterY), 0])
    visited = [[0]*51 for _ in range(51)]
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    while queue:
        cur_loc, level = queue.popleft()
        visited[cur_loc[0]][cur_loc[1]] = 1

        if cur_loc == (itemX, itemY):
            break

        for k in range(4):
            next_loc = (cur_loc[0] + di[k], cur_loc[1] + dj[k])

            if visited[next_loc[0]][next_loc[1]]:
                continue

            cur_box = []

            # 현재 테두리 위에 있는 직사각형 저장
            for rect in rectangle:
                if next_loc[0] in [rect[0], rect[2]] and next_loc[1] in range(rect[1], rect[3] + 1) or\
                    next_loc[0] in range(rect[0], rect[2] + 1) and next_loc[1] in [rect[1], rect[3]]:
                    cur_box.append(rect)
                else:
                    continue

            if len(cur_box) == 0:
                continue

            # 그 외에 다른 상자 내부에 있나 확인
            for r in rectangle:
                if r not in cur_box:
                    if next_loc[0] in range(r[0] + 1, r[2]) or next_loc[1] in range(r[1] + 1, r[3]):
                        break
                    else:
                        continue
            else:
                queue.append([next_loc, level + 1])

    return level


print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))     # 17
print(solution([[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]], 9, 7, 6, 1))     # 11
print(solution([[1, 1, 5, 7]], 1, 1, 4, 7))     # 9
print(solution([[2, 1, 7, 5], [6, 4, 10, 10]], 3, 1, 7, 10))     # 15
print(solution([[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]], 1, 4, 6, 3))     # 10
