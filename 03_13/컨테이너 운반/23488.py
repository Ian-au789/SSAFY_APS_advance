# https://swexpertacademy.com/main/talk/solvingClub/problemBoxDetail.do?solveclubId=AZTP1QzqXnbHBIRD&probBoxId=AZVkSAOaDP_HBINE&leftPage=1

import sys
sys.stdin = open("sample_input(3).txt")
import heapq

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    cargo = list(map(int, input().split()))
    load = list(map(int, input().split()))
    negative = [c * -1 for c in cargo]
    heapq.heapify(negative)
    weight = 0
    load.sort(reverse=True)

    for truck in load:
        if len(negative) == 0:
            break

        while truck < -1 * negative[0]:
            heapq.heappop(negative)

            if len(negative) == 0:
                break

        if len(negative) == 0:
            break

        weight += -1 * negative[0]
        heapq.heappop(negative)

    print(f"#{t} {weight}")
