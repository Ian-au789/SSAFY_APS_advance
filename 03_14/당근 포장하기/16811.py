# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AYamNLoKGSgDFAVx&probBoxId=AZVkSAOaDQDHBINE&type=USER&problemBoxTitle=%2803.14%29+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B42&problemBoxCnt=4

import sys
sys.stdin = open("sample_in.txt")


T = int(input())
for t in range(1, T+1):
    N = int(input())
    carrots = list(map(int, input().split()))
    small = 0
    medium = 0
    large = 0

    for i in range(N - 1):
        if 0 <= i < N // 2:
            small += 1
