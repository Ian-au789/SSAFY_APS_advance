# https://source-sc.tistory.com/59

import sys
sys.stdin = open("sample_input(4).txt")

T = int(input())
for t in range(1, T+1):
    N = int(input())
    hours = [list(map(int, input().split())) for _ in range(N)]
    schedule = [0] * 24
    cnt = 0

    hours.sort(key=lambda x: x[1])     # 끝나는 시간 순서대로 정렬

    for hour in hours:
        for k in range(hour[0], hour[1]):       # 스케줄표가 비어있나 확인
            if schedule[k]:
                break

        else:
            cnt += 1
            for k in range(hour[0], hour[1]):   # 스케줄표에 기입
                schedule[k] = 1

    print(f"#{t} {cnt}")
