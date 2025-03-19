# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV15StKqAQkCFAYD&probBoxId=AZVkSAOaDQTHBINE&type=PROBLEM&problemBoxTitle=%2803.20%29++%EA%B7%B8%EB%9E%98%ED%94%842&problemBoxCnt=5

import sys
sys.stdin = open("input.txt")

T = int(input())
for t in range(1, T+1):
    N = int(input())
    loc_i = list(map(int, input().split()))
    loc_j = list(map(int, input().split()))
    E = int(input())

    island = []
    for k in range(N):
        island.append((loc_i[k], loc_j[k]))
    dist = 0

    print(f"#{t} {E * dist}")