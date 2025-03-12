# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV15Khn6AN0CFAYD&probBoxId=AZVkSAOaDP7HBINE&type=PROBLEM&problemBoxTitle=%2803.12%29+%EC%99%84%EC%A0%84%ED%83%90%EC%83%89+%EB%B0%8F+%EA%B7%B8%EB%A6%AC%EB%94%941&problemBoxCnt=5

import sys
sys.stdin = open("input.txt")


def max_prize(card_list, left):
    global money

    # 상금 구하기
    if left == 0:
        prize = 0
        digit = 0
        for c in card_list[::-1]:
            prize += c * 10 ** digit
            digit += 1

        if prize > money:    # 최댓값 갱신
            money = prize
        return

    for i in range(len(card_list)-1):
        if card_list[i] == max(card_list[i:]):           # 가장 큰 자릿수 숫자가 이미 가장 큰 숫자이면 바꾸지 않음
            continue

        for j in range(i+1, len(card_list)):             # 본인 자릿수 뒤에 있는 숫자 중 가장 큰 숫자와 교환
            if card_list[j] == max(card_list[i+1:]):
                cards = [n for n in card_list]
                cards[i], cards[j] = cards[j], cards[i]
                max_prize(cards, left - 1)

    # 이미 가능한 가장 큰 숫자에 도달한 경우
    if len(set(card_list)) != len(card_list):        # 중복되는 숫자가 있으면 그 숫자끼리 교환하면서 최댓값 유지
        return max_prize(card_list, 0)

    if left == 1:
        cards = [n for n in card_list[::-1]]
        cards[0], cards[1] = cards[1], cards[0]
        return max_prize(cards[::-1], left - 1)      # 교환 횟수가 1번 남으면 가장 작은 자릿수 2개 교환

    else:
        return max_prize(card_list, left - 2)        # 아무 숫자끼리 2번 교환하면서 최댓값 유지


T = int(input())
for t in range(1, T+1):
    number, change = map(str, input().split())

    original_cards = [int(n) for n in number]
    change = int(change)
    money = 0

    max_prize(original_cards, change)
    print(f"#{t} {money}")
