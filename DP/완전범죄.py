# https://school.programmers.co.kr/learn/courses/30/lessons/389480


# BFS 완전탐색은 당연히 모든 경우를 찾을 수 있지만 시간복잡도가 2^N으로 겁나 오래걸림
from collections import deque


def bfs(info, n, m):
    size = len(info)

    queue = deque()
    if info[0][0] < n:
        queue.append((info[0][0], 0, 0))
    if info[0][1] < m:
        queue.append((0, info[0][1], 0))

    result = 1e9

    while queue:
        trace_a, trace_b, idx = queue.popleft()

        if idx < size - 1:
            if trace_a + info[idx + 1][0] < n:
                queue.append((trace_a + info[idx + 1][0], trace_b, idx + 1))

            if trace_b + info[idx + 1][1] < m:
                queue.append((trace_a, trace_b + info[idx + 1][1], idx + 1))

        else:
            if result > trace_a:
                result = trace_a

    if result == 1e9:
        return -1

    return result


# DP를 쓰면 시간복잡도가 N*M으로 순식간에 해결
def solution(info, n, m):
    size = len(info)
    dp = [[1000] * m for _ in range(size)]

    # 첫 번째 물건 훔친 2가지 경우로 시작
    if info[0][0] < n:
        dp[0][0] = info[0][0]
    if info[0][1] < m:
        dp[0][info[0][1]] = 0

    for i in range(size - 1):
        a, b = info[i+1][0], info[i+1][1]

        for j in range(m):
            if dp[i][j] == 1000:
                continue

            if dp[i][j] + a < n:
                dp[i+1][j] = min(dp[i][j] + a, dp[i+1][j])    # A가 물건을 훔친 경우
            if j + b < m:
                dp[i+1][j+b] = min(dp[i][j], dp[i+1][j+b])    # B가 물건을 훔친 경우

    result = min(dp[size - 1])

    if result == 1000:
        return -1
    else:
        return result


print(solution([[1, 2], [2, 3], [2, 1]], 4, 4))
print(solution([[1, 2], [2, 3], [2, 1]], 1, 7))
print(solution([[3, 3], [3, 3]], 7, 1))
print(solution([[3, 3], [3, 3]], 6, 1))
