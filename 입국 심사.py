# https://school.programmers.co.kr/learn/courses/30/lessons/43238

# 2020 세체미 쇼메이커

def solution(n, times):
    start = 0
    end = max(times) * n
    mid = (start + end) // 2
    path = []

    while 1:
        check = 0
        for time in times:
            check += mid // time

        if check >= n:
            path.append(mid)
            end = mid

        elif check < n:
            start = mid

        mid = (start + end) // 2

        if start == mid or mid == end:
            return path.pop()


print(solution(6, [7, 10]))
