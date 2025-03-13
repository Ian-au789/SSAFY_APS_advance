# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZT4zs56TIvHBIOK&probBoxId=AZVkSAOaDP_HBINE&type=USER&problemBoxTitle=%2803.13%29+%EC%99%84%EC%A0%84%ED%83%90%EC%83%89+%EB%B0%8F+%EA%B7%B8%EB%A6%AC%EB%94%942&problemBoxCnt=4

import sys
sys.stdin = open("sample_input(4).txt")

T = int(input())
for t in range(1, T+1):
    N = int(input())
    hours = [list(map(int, input().split())) for _ in range(N)]
    schedule = [0] * 24
    cnt = 0

    hours.sort(key=lambda x: (x[1] - x[0]))     # 작업시간 순서대로 정렬

    for hour in hours:
        for k in range(hour[0], hour[1]):       # 스케줄표가 비어있나 확인
            if schedule[k]:
                break

        else:
            cnt += 1
            for k in range(hour[0], hour[1]):   # 스케줄표에 기입
                schedule[k] = 1

    print(f"#{t} {cnt}")

# 이거 하면 안돼 (반례 : [11, 13], [0, 12], [12,23])
