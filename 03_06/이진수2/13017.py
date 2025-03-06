# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AXwz6r6qAKUDFASZ&probBoxId=AZVkSAOaDPrHBINE&type=USER&problemBoxTitle=%2803.06%29+start+1&problemBoxCnt=4

import sys
sys.stdin = open("sample_input(18).txt")


T = int(input())
for t in range(1, T+1):
    N = float(input())

    result = ""
    # n = -1
    #
    # while N > 0:
    #     if N >= 2 ** n:
    #         N -= 2 ** n
    #         result += "1"
    #
    #     else:
    #         result += "0"
    #
    #     n -= 1
    #
    #     if len(result) > 13:
    #         result = "overflow"
    #         break

    while N > 0:
        N *= 2

        if N >= 1:
            N -= 1
            result += "1"

        else:
            result += "0"

        if len(result) == 13:
            result = "overflow"
            break

    print(f"#{t} {result}")
