import sys
sys.stdin = open("sample_input.txt")


T = int(input())
for t in range(1, T+1):
    N, W = map(int, input().split())
    elements = list(map(int, input().split()))

    dp = [0] * (W+1)       # 부분 집합의 합을 인덱스로 가지는 배열
    dp[0] = 1              # 공집합 가능한 경우 1개

    for e in elements:
        for i in range(W, e-1, -1):       # 중복 방지를 위해 뒤에서부터 탐색
            dp[i] += dp[i - e]

    print(f"#{t} {dp[W]}")
