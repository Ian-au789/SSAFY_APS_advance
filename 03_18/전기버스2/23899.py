# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZVkZGPKDvDHBINE&probBoxId=AZVkSAOaDQLHBINE&type=USER&problemBoxTitle=%2803.18%29++%EB%B6%84%ED%95%A0%EC%A0%95%EB%B3%B5+%EB%B0%8F+%EB%B0%B1%ED%8A%B8%EB%9E%98%ED%82%B92&problemBoxCnt=5

import sys
sys.stdin = open("5208_input.txt")


def electric_bus(battery, idx, end, time):
    global result
    if idx == end:
        result = min(result, time)       # 배터리 교체 횟수 최솟값 갱신

    if time >= result:
        return

    if idx > 0:   # 처음에는 배터리 교체 X
        electric_bus(station[idx] - 1, idx + 1, end, time + 1)   # 배터리 교체하고 이동

    if battery > 0:   # 배터리가 바닥나면 진행 불가
        electric_bus(battery - 1, idx + 1, end, time)    # 배터리 교체 안하고 이동


T = int(input())
for t in range(1, T+1):
    station = list(map(int, input().split()))
    N = station.pop(0)
    result = N
    electric_bus(station[0], 0, N - 1, 0)

    print(f"#{t} {result}")
