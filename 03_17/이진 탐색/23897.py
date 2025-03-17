# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZVkYDD6DqPHBINE&probBoxId=AZVkSAOaDQHHBINE&type=USER&problemBoxTitle=%2803.17%29++%EB%B6%84%ED%95%A0%EC%A0%95%EB%B3%B5+%EB%B0%8F+%EB%B0%B1%ED%8A%B8%EB%9E%98%ED%82%B91&problemBoxCnt=6

import sys
sys.stdin = open("5207_input.txt")


def bin_search(num):
    global N
    start = 0
    end = N - 1

    while start <= end:
        mid = (start + end) // 2

        if N_list[mid] == num:
            return 1

        elif N_list[mid] > num:
            end = mid - 1
        else:
            start = mid + 1

    return 0


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    N_list = sorted(list(map(int, input().split())))
    M_list = list(map(int, input().split()))

    result = 0
    for m in M_list:
        result += bin_search(m)

    print(f"#{t} {result}")
