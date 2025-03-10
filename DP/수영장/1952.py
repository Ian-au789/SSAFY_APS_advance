# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV5PpFQaAQMDFAUq&probBoxId=AZTeuPGad_vHBIOK&type=PROBLEM&problemBoxTitle=A%ED%98%95+%EC%97%AD%EB%9F%89%ED%85%8C%EC%8A%A4%ED%8A%B8+%EB%AA%A8%EC%9D%8C%EC%A7%91+&problemBoxCnt=20

import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for t in range(1, T+1):
    price = list(map(int, input().split()))
    month = list(map(int, input().split()))

    dp = [0] * 12
    dp[0] = min(price[0] * month[0], price[1])      # 초기값 설정
    dp[1] = min(dp[0] + price[0] * month[1], dp[0] + price[1])
    dp[2] = min(dp[1] + price[0] * month[2], dp[1] + price[1], price[2])

    for i in range(1, 12):
        # 1일 이용권만 쓰는 경우, 한달 이용권 쓰는 경우, 3달 전에 3개월 이용권을 끊은 경우 비교
        dp[i] = min(dp[i-1] + price[0] * month[i], dp[i-1] + price[1], dp[i-3] + price[2])

    print(f"#{t} {min(dp[11], price[3])}")
