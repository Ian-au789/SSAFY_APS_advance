# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZVkS-HqDUvHBINE&probBoxId=AZVkSAOaDPvHBINE&type=USER&problemBoxTitle=%2803.07%29+start+2&problemBoxCnt=4

import sys
sys.stdin = open("hex_dec_input.txt")

T = int(input())
for t in range(1, T+1):
    hex_num = list(map(str, input()))

    bin_num = ""
    for h in hex_num:
        h_b = str(bin(int(h, 16))[2:])

        if len(h_b) < 4:
            bin_num += "0" * (4 - len(h_b))

        bin_num += h_b

    idx = 0
    int_num = []
    N = len(bin_num)
    while idx < N:
        if idx + 7 <= N:
            int_num.append(int(bin_num[idx:idx + 7], 2))
            idx += 7

        else:
            i = N - idx
            int_num.append(int(bin_num[idx:idx + i], 2))
            idx += i

    result = " ".join(map(str, int_num))
    print(f"#{t} {result}")
