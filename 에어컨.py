# https://school.programmers.co.kr/learn/courses/30/lessons/214289

'''
temperature = 실외 온도 이자 0분 시점 실내 온도
1. 에어컨의 전원을 키면 실내 온도가 희망 온도에 1분마다 1도씩 가까워짐, 희망 온도에 도달하면 해당 온도 유지
2. 에어컨의 전원이 꺼지면 실내 온도가 실외 온도에 1분마다 1도씩 가까워짐
3. 희망 온도와 실내 온도가 다르면 매분 a만큼, 같아면 매분 b만큼 전력 소비
'''

def solution(temperature, t1, t2, a, b, onboard):
    temperature, t1, t2 = temperature + 10, t1 + 10, t2 + 10     # 음수 인덱스 방지

    size = len(onboard)
    dp = [[int(1e9)]*51 for _ in range(size)]    # i축은 시간선, j축은 온도를 나타냄
    dp[0][temperature] = 0          # 시작 온도에서는 비용이 0

    if temperature < t1:            # 에어컨 전원이 꺼져 있으면 온도가 내려감
        for i in range(size - 1):
            for j in range(temperature, t2 + 1):             # 온도는 실외 온도와 t2 사이를 벗어나지 않음
                if onboard[i] and not (t1 <= j <= t2):       # 승객이 차에 타고 있으면 반드시 적정온도를 유지해야함
                    continue

                if dp[i][j] == 1e9:        # 해당 온도에 도달한 적 없으면 pass
                    continue

                if j == temperature:           # case 1) 온도가 변하지 않거나 올라감
                    dp[i+1][j] = min(dp[i+1][j], dp[i][j])
                    dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j] + a)

                elif temperature < j < t1:     # case 2) 온도가 떨어지거나 올라감
                    dp[i+1][j-1] = min(dp[i+1][j-1], dp[i][j])
                    dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j] + a)

                elif t1 <= j < t2:             # case 3) 온도가 떨어지거나 희망온도 유지, 또는 상승
                    dp[i + 1][j - 1] = min(dp[i + 1][j - 1], dp[i][j])
                    dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + b)
                    dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j] + a)

                else:                          # case 4) 온도가 희망온도를 유지하거나 떨어짐
                    dp[i+1][j-1] = min(dp[i + 1][j - 1], dp[i][j])
                    dp[i+1][j] = min(dp[i+1][j], dp[i][j] + b)

            if onboard[i + 1]:
                for j in range(temperature, t2 + 1):
                    if not (t1 <= j <= t2):
                        dp[i + 1][j] = int(1e9)

    elif t1 <= temperature <= t2:   # 에어컨 전원이 꺼져도 항상 적정온도 유지
        return 0

    else:        # 부호 반대로 진행
        for i in range(size - 1):
            for j in range(t1, temperature + 1):
                if onboard[i] and not (t1 <= j <= t2):
                    continue

                if dp[i][j] == 1e9:
                    continue

                if j == temperature:
                    dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
                    dp[i + 1][j - 1] = min(dp[i + 1][j - 1], dp[i][j] + a)
                    continue

                elif t2 < j < temperature:
                    dp[i + 1][j - 1] = min(dp[i + 1][j - 1], dp[i][j] + a)
                    dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j])

                elif t1 < j <= t2:
                    dp[i + 1][j - 1] = min(dp[i + 1][j - 1], dp[i][j] + a)
                    dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + b)
                    dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j])

                else:
                    dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j])
                    dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + b)

            if onboard[i + 1]:
                for j in range(t1, temperature + 1):
                    if not (t1 <= j <= t2):
                        dp[i + 1][j] = int(1e9)

    return min(dp[size - 1])

print(solution(28, 18, 26, 10, 8, [0, 0, 1, 1, 1, 1, 1]))   # 40
print(solution(-10, -5, 5, 5, 1, [0, 0, 0, 0, 0, 1, 0]))   # 25
print(solution(11, 8, 10, 10, 1, [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1]))  # 20
print(solution(11, 8, 10, 10, 100, [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1]))  # 60
