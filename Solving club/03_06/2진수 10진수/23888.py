# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZVkSWq6DRbHBINE&probBoxId=AZVkSAOaDPrHBINE&type=USER&problemBoxTitle=%2803.06%29+start+1&problemBoxCnt=4

import sys
sys.stdin = open("start_input.txt")


def ten_digit(two_digit):
    n = 0
    ten = 0
    for b in two_digit[::-1]:
        ten += b * 2 ** n
        n += 1

    return ten


T = int(input())
for t in range(1, T+1):
    N = int(input())
    digits = ""
    for _ in range(N):
        digits += input().strip()

    converted = []

    idx = 0
    while idx < len(digits):
        converted.append(ten_digit(list(map(int, digits[idx:idx+7]))))
        idx += 7

    result = " ".join(map(str, converted))

    print(f"#{t} {result}")
