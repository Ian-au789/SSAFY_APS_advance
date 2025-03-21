import sys
sys.stdin = open("input.txt")


def dfs(used, row):
    if row == N:  # 모든 행을 선택한 경우
        return 1  # 곱셈을 위해 1 반환

    if dp[used] != -1:  # 이미 계산된 경우 반환
        return dp[used]

    max_prob = 0
    for col in range(N):
        if not (used & (1 << col)):  # 아직 선택하지 않은 열
            prob = arr[row][col] / 100
            if prob > 0:  # 가지치기 (0이면 탐색 불필요)
                max_prob = max(max_prob, prob * dfs(used | (1 << col), row + 1))

    dp[used] = max_prob  # 메모이제이션 저장
    return dp[used]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dp = [-1] * (1 << N)  # DP 테이블 초기화 (비트마스크 사용)

    result = dfs(0, 0) * 100  # 0번 행부터 탐색 시작
    print(f'#{tc} {result:.6f}')  # 소수점 6자리 출력
