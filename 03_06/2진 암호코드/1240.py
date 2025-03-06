# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV15FZuqAL4CFAYD&probBoxId=AZVkSAOaDPrHBINE&type=PROBLEM&problemBoxTitle=%2803.06%29+start+1&problemBoxCnt=4

import sys
sys.stdin = open("input.txt")


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [input() for _ in range(N)]          # 입력값 받기

    signal = ""
    for row in matrix:
        if sum(list(map(int, row))) > 0:          # 암호가 들어있는 행 탐색
            signal += row
            break

    # 해독 준비
    code = []
    cypher = {"0001101": 0, "0011001": 1, "0010011": 2, "0111101": 3, "0100011": 4,
              "0110001": 5, "0101111": 6, "0111011": 7, "0110111": 8, "0001011": 9}

    idx = 0
    check = 0
    while idx + 1:
        if signal[idx:idx + 7] in cypher and check == 0:        # 암호가 처음 발견되었을 때
            if signal[idx + 7:idx + 14] in cypher:              # 그 다음 암호도 존재하는 지 확인
                check = 1
                code.append(cypher[signal[idx:idx + 7]])        # 해독한 암호 저장
                idx += 7                                        # 다음 암호 해독 위해 7칸 전진
            else:
                idx += 1

        elif signal[idx:idx + 7] in cypher and check == 1:
            code.append(cypher[signal[idx:idx + 7]])
            idx += 7

        elif check == 0 and signal[idx:idx + 7] not in cypher:  # 암호를 찾을 때 까지 한 칸씩 전진
            if len(code) > 0:
                break
            else:
                idx += 1

        else:                                                   # 해독 완료하면 break
            break

    odd = sum([code[i] for i in range(len(code)) if i % 2 == 0])       # 홀수 자리의 합
    even = sum([code[i] for i in range(len(code)) if i % 2 == 1])      # 짝수 자리의 합

    # 올바른 암호면 해독 결과 출력, 그렇지 않으면 0 출력
    if (odd * 3 + even) % 10 == 0:
        result = sum(code)

    else:
        result = 0

    print(f"#{t} {result}")
