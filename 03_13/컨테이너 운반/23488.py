# https://swexpertacademy.com/main/talk/solvingClub/problemBoxDetail.do?solveclubId=AZTP1QzqXnbHBIRD&probBoxId=AZVkSAOaDP_HBINE&leftPage=1

import sys
sys.stdin = open("sample_input(3).txt")
import heapq

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    cargo = list(map(int, input().split()))
    load = list(map(int, input().split()))

    # cargo 값을 음수로 바꿔서 힙으로 관리
    negative = [-c for c in cargo]
    heapq.heapify(negative)

    weight = 0
    load.sort(reverse=True)

    # load에 있는 트럭들에 대해서 처리
    for truck in load:
        # 트럭의 무게보다 작은 화물이 없다면 더 이상 트럭을 채울 수 없음
        while negative and truck < -negative[0]:
            heapq.heappop(negative)

        if not negative:
            break

        # 가장 큰 화물 적재
        weight += -negative[0]
        heapq.heappop(negative)

    print(f"#{t} {weight}")
