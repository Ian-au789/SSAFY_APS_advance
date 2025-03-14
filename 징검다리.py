# https://school.programmers.co.kr/learn/courses/30/lessons/43236

# 역체미 페이커


def solution(distance, rocks, n):
    rocks.sort()
    between = [rocks[0]]
    for i in range(1, len(rocks)):
        between.append(rocks[i] - rocks[i - 1])
    between.append(distance - rocks[len(rocks) - 1])
    size = len(between)

    start = 0
    end = distance
    mid = (start + end) // 2
    path = []                # 최솟값 이하의 값들을 저장

    while 1:
        min_dist = 1
        idx = 0
        chance = n

        while idx < size:
            d = between[idx]           # 바위 사이의 거리 확인
            if d >= mid:               # 바위 거리가 최솟값보다 크다면 넘어가기
                idx += 1

            else:
                # 바위 사이의 거리가 최솟값보다 작다면 바위를 제거해서 거리 더하기
                while idx < size and chance > 0 and d < mid:     # 바위 제거 횟수, 인덱스 에러 방지, 최솟값 이하 확인
                    idx += 1
                    d += between[idx]
                    chance -= 1
                idx += 1

                if d < mid:           # 바위 제거를 다 했어도 최솟값보다 작은 바위 사리 거리가 있다면 최솟값이 아님
                    min_dist = 0
                    break

        if min_dist:        # 최솟값이 맞다면 저장하고 시작점 조정
            path.append(mid)
            start = mid

        else:               # 최솟값이 아니라면 도착점 조정
            end = mid

        mid = (start + end) // 2  # 중간값 업데이트

        if start == mid or mid == end:  # 탐색 불가능한 지점에 도달하면
            return path.pop()  # 가장 정답에 근접했던 값 반환


print(solution(25, [2, 14, 11, 21, 17], 2))
