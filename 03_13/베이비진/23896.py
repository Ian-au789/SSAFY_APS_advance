# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZVkWq0aDl7HBINE&probBoxId=AZVkSAOaDP_HBINE&type=USER&problemBoxTitle=%2803.13%29+%EC%99%84%EC%A0%84%ED%83%90%EC%83%89+%EB%B0%8F+%EA%B7%B8%EB%A6%AC%EB%94%942&problemBoxCnt=4

import sys
sys.stdin = open("5203_input.txt")


def baby_gin(cards):
    cards = sorted(cards)
    stack = [cards[0]]
    top = 0
    cnt = 0

    for i in range(1, len(cards)):

        if cards[i] == stack[top]:    # 같은 카드는 스택에 입력하지 않고 카운트
            cnt += 1

        else:
            stack.append(cards[i])    # 다른 카드는 스택에 입력 후 카운트 초기화
            top += 1
            cnt = 0

        if cnt == 2:    # triplet 검사
            return 1

        if top > 1:
            if stack[top] == stack[top - 1] + 1 == stack[top - 2] + 2:      # run 검사
                return 1

    else:
        return 0


T = int(input())
for t in range(1, T+1):
    c = list(map(int, input().split()))
    player1 = [c[0], c[2]]
    player2 = [c[1], c[3]]
    result = 0

    for i in range(2, 6):
        player1.append(c[2 * i])
        player2.append(c[2 * i + 1])

        if baby_gin(player1):        # 카드 추가할 때 마다 확인
            result = 1
            break
        if baby_gin(player2):
            result = 2
            break

    print(f"#{t} {result}")
