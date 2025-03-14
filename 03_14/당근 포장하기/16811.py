# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AYamNLoKGSgDFAVx&probBoxId=AZVkSAOaDQDHBINE&type=USER&problemBoxTitle=%2803.14%29+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B42&problemBoxCnt=4

import sys
sys.stdin = open("sample_in.txt")


def pack_carrots(numbers, size):
    result = 1000
    end = len(numbers)

    for i in range(1, end - 1):
        for j in range(i+1, end):
            small = sum(numbers[:i])
            medium = sum(numbers[i:j])
            large = sum(numbers[j:])

            if small == 0 or medium == 0 or large == 0:         # 조건에 안 맞는 경우 넘기기
                continue
            if small > N // 2 or medium > N // 2 or large > N // 2:
                continue

            box = [small, medium, large]
            result = min(result, max(box) - min(box))

    if result == 1000:
        return -1

    return result


T = int(input())
for t in range(1, T+1):
    N = int(input())
    carrots = list(map(int, input().split()))
    stock = [0] * (max(carrots) + 1)           # 당근 크기에 따라 당근 개수 배열에 저장

    for c in carrots:
        stock[c] += 1

    print(f"#{t} {pack_carrots(stock, N)}")
