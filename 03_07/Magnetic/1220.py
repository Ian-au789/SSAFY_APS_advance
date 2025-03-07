# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV14hwZqABsCFAYD&probBoxId=AZVkSAOaDPvHBINE&type=PROBLEM&problemBoxTitle=%2803.07%29+start+2&problemBoxCnt=4

import sys
sys.stdin = open("input.txt")


for t in range(1, 11):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    matrix_t = list(map(list, zip(*matrix)))                    # 전치 쓰면 편함 (내가)

    cnt = 0     # 교착 상태 세기

    for row in matrix_t:
        stack = []         # 스택 준비
        top = -1
        idx = 0

        while idx < N:                           # 행 탐색
            if row[idx]:
                stack.append(row[idx])           # 자성체를 발견하면 입력
                top += 1

                if row[idx] == 2 and top > 0:
                    if stack[top] != stack[top-1]:   # 1뒤에 2가 나타났다면 교착상태
                        cnt += 1
            idx += 1

    print(f"#{t} {cnt}")
