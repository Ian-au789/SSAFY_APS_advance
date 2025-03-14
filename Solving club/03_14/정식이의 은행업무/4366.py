# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AWMeRLz6kC0DFAXd&probBoxId=AZVkSAOaDQDHBINE&type=PROBLEM&problemBoxTitle=%2803.14%29+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B42&problemBoxCnt=4

import sys
sys.stdin = open("sample_input.txt")


T = int(input())
for t in range(1, T+1):
    o_two = list(map(int, input()))
    o_three = list(map(int, input()))
    result = 0

    for i in range(len(o_two)):
        o_two[i] = (o_two[i] + 1) % 2       # 2진수 자릿수 하나씩 바꾸기 (0, 1)

        for j in range(len(o_three)):
            # 3진수 자릿수 한 번 바꾸기 (0, 1, 2)
            o_three[j] = (o_three[j] + 1) % 3
            if int("".join(map(str, o_two)), 2) == int("".join(map(str, o_three)), 3):    # 바꾼 2진수와 3진수가 일치하나 확인
                result = int("".join(map(str, o_two)), 2)
                break

            # 3진수 자릿수 한 번 더 바꾸기 (0, 1, 2)
            o_three[j] = (o_three[j] + 1) % 3
            if int("".join(map(str, o_two)), 2) == int("".join(map(str, o_three)), 3):
                result = int("".join(map(str, o_two)), 2)
                break

            o_three[j] = (o_three[j] + 1) % 3    # 바꾼 3진수 원상복귀

        if result > 0:
            break

        o_two[i] = (o_two[i] + 1) % 2       # 바꾼 2진수 원상복귀

    print(f"#{t} {result}")
