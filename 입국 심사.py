# https://school.programmers.co.kr/learn/courses/30/lessons/43238

# 2020 세체미 쇼메이커

def solution(n, times):
    start = 0
    end = max(times) * n
    mid = (start + end) // 2
    path = []      # 정답 이상의 값들 저장

    while 1:
        # 해당 시각에 입국 심사 통과하는 사람 수 검사
        check = 0
        for time in times:
            check += mid // time

        if check >= n:              # 정답 이상이면 저장하고 끝값 조정
            path.append(mid)
            end = mid

        elif check < n:             # 정답 보다 적으면 시작값 조정
            start = mid

        mid = (start + end) // 2    # 중간값 업데이트

        if start == mid or mid == end:    # 탐색 불가능한 지점에 도달하면
            return path.pop()             # 가장 정답에 근접했던 값 반환


print(solution(6, [7, 10]))
