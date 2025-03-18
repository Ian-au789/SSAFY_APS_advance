# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV5V4A46AdIDFAWu&probBoxId=AZVkSAOaDQLHBINE&type=PROBLEM&problemBoxTitle=%2803.18%29++%EB%B6%84%ED%95%A0%EC%A0%95%EB%B3%B5+%EB%B0%8F+%EB%B0%B1%ED%8A%B8%EB%9E%98%ED%82%B92&problemBoxCnt=5

import sys
sys.stdin = open("sample_input.txt")


def honey_price(size, limit, honey):
    if sum(honey) <= limit:
        return sum([h ** 2 for h in honey])     # 벌꿀이 최대용량을 초과하지 않으면 전부 계산

    else:
        max_price = 0
        for i in range(1 << size):              # 비트마스크를 써서 모든 경우의 수 계산
            price = 0
            check = 0
            for j in range(size):
                if i & (1 << j):
                    price += honey[j] ** 2
                    check += honey[j]

            if check <= limit:                 # 최대용량을 넘는 경우는 제외
                max_price = max(max_price, price)

        return max_price


T = int(input())
for t in range(1, T+1):
    N, M, C = map(int, input().split())
    beehive = [list(map(int, input().split())) for _ in range(N)]

    # M개의 벌통을 골랐을 때 판매 금액 계산해서 저장
    row = N - M + 1
    honey_money = [[0] * row for _ in range(N)]

    for i in range(N):
        for j in range(row):
            sell = []
            for k in range(M):
                sell.append(beehive[i][j+k])

            honey_money[i][j] = honey_price(M, C, sell)

    # 일꾼이 돌아다니며 벌꿀 채취
    result = 0
    patt = 0
    matt = 0
    for i in range(N):
        for j in range(row):
            patt = honey_money[i][j]

            if j + M <= N - M:          # 같은 열에서 아직 공간이 남으면 행 탐색
                for k in range(j+M, row):
                    matt = honey_money[i][k]
                    result = max(result, patt + matt)

            for m in range(i+1, N):     # 다음 행으로 넘어가서 탐색
                for n in range(row):
                    matt = honey_money[m][n]
                    result = max(result, patt + matt)

    print(f"#{t} {result}")
