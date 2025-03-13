# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AXwz50maAI4DFASZ&probBoxId=AZVkSAOaDPrHBINE&type=USER&problemBoxTitle=%2803.06%29+start+1&problemBoxCnt=4

import sys
sys.stdin = open("sample_input(17).txt")

T = int(input())
for t in range(1, T+1):
    N, hex_digit = map(str, input().split())
    result = ""

    for n in range(int(N)):
        binary = str(bin(int(hex_digit[n], 16))[2:])

        if len(binary) < 4:
            temp = "0" * (4-len(binary))
            result += temp

        result += binary

    print(f'#{t} {result}')
