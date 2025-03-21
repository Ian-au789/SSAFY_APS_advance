# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AXuUo_Tqs9kDFARa&probBoxId=AZVkSAOaDQXHBINE&type=PROBLEM&problemBoxTitle=%2803.21%29++%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B43&problemBoxCnt=5

import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for t in range(1, T+1):
    A, B, C, D = map(int, input().split())
    X, Y = 0, 0

    for i in range(A, B):
        X = X | (1 << i)
    for j in range(C, D):
        Y = Y | (1 << j)

    cnt = 0
    for k in range(101):
        if X & Y & (1 << k):
            cnt += 1

    print(f"#{t} {cnt}")
