# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AY3jpQ8qXZ8DFARM&probBoxId=AZVkSAOaDPzHBINE&type=USER&problemBoxTitle=%2803.10%29+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4&problemBoxCnt=4

from collections import deque
import sys
sys.stdin = open("input.txt")


def shuffle(cards, size):
    overhead = int(0.37 * size)

    for _ in range(overhead):      # 오버헤드 셔플 진행
        temp = cards.pop()
        cards.appendleft(temp)

    odd = deque()
    even = deque()
    shuffled = deque()

    for m in range(size):          # 퍼펙트 셔플 진행
        if size % 2 == 0:
            if m < size // 2:
                even.append(cards[m])
            else:
                odd.append(cards[m])
        else:
            if m <= size // 2:
                even.append(cards[m])
            else:
                odd.append(cards[m])

    for n in range(size):
        if n % 2 == 0:
            shuffled.append(even[n // 2])
        else:
            shuffled.append(odd[n // 2])

    return shuffled


TC = int(input())
for t in range(1, TC+1):
    N, T = map(int, input().split())
    card_deck = deque()

    for i in range(1, N + 1):
        card_deck.append(i)

    for _ in range(T):
        card_deck = shuffle(card_deck, N)

    result = " ".join(map(str, card_deck))
    print(f"#{t} {result}")
