# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZVkTOzaDWbHBINE&probBoxId=AZVkSAOaDPvHBINE&type=USER&problemBoxTitle=%2803.07%29+start+2&problemBoxCnt=4

import sys
sys.stdin = open("bit_input.txt")


T = int(input())
for t in range(1, T+1):
    code = {"001101": 0, "010011": 1, "111011": 2, "110001": 3, "100011": 4,
            "110111": 5, "001011": 6, "111101": 7, "011001": 8, "101111": 9}

    hex_num = list(map(str, input().strip()))

    bin_num = ""
    for h in hex_num:
        h_b = str(bin(int(h, 16))[2:])

        if len(h_b) < 4:
            bin_num += "0" * (4 - len(h_b))

        bin_num += h_b

    N = len(bin_num)
    idx = 6
    solved = []

    while idx < N:
        if bin_num[idx-6:idx] not in code:
            idx += 1
        else:
            solved.append(code[bin_num[idx-6:idx]])
            idx += 6

    result = " ".join(map(str, solved))

    print(f"#{t} {result}")
