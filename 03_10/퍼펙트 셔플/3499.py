# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AWGsRbk6AQIDFAVW&probBoxId=AZVkSAOaDPzHBINE&type=PROBLEM&problemBoxTitle=%2803.10%29+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4&problemBoxCnt=4

import sys
sys.stdin = open("sample_input.txt")


T = int(input())
for t in range(1, T+1):
    N = int(input())
    cards = list(map(str, input().split()))

    odd = []
    even = []
    shuffled = []

    for m in range(N):          # 퍼펙트 셔플 진행
        if N % 2 == 0:
            if m < N // 2:
                even.append(cards[m])
            else:
                odd.append(cards[m])
        else:
            if m <= N // 2:
                even.append(cards[m])
            else:
                odd.append(cards[m])

    for n in range(N):
        if n % 2 == 0:
            shuffled.append(even[n // 2])
        else:
            shuffled.append(odd[n // 2])

    result = " ".join(shuffled)

    print(f"#{t} {result}")
