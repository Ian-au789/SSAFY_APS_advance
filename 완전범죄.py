# https://school.programmers.co.kr/learn/courses/30/lessons/389480

'''
1. 도둑이 물건 n을 훔치면 A는 info[n][0], B는 info[n][1] 만큼 흔적
2. 누적된 흔적의 합계가 각각 m, n 이상이면 검거
3. 잡히지않고 모든 물건을 훔치는 경우, A가 남기는 누적 개수의 최솟값 return.
4. 검거되지 않고 모든 물건을 훔치기 불가능하면 -1 return
점화식 : dp_a[i][j + a_trace] = min(dp_a[i - 1][j + a_trace], dp_a[i-1][j] + a_trace)
'''


def solution(info, n, m):
    size = len(info)

    dp = [[[float('inf'), 0] for _ in range(n + 1)] for _ in range(size + 1)]
    dp[0][0] = [0, 0]

    for i in range(1, size + 1):
        a, b = info[i - 1]  # i번째 물건에 대한 흔적

        if a < n or b < m:
            for j in range(n - a):
                if dp[i - 1][j + a][0] < dp[i-1][j][0] + a:
                    dp[i][j + a][0] = dp[i - 1][j + a][0]
                    dp[i][j + a][1] = dp[i - 1][j + a - b][1] + b

                else:
                    dp[i][j + a][0] = dp[i-1][j][0] + a
                    dp[i][j + a][1] = dp[i - 1][j + a - b][1]

        else:
            return -1

    print(dp)


print(solution([[1, 2], [2, 3], [2, 1]], 4, 4))
