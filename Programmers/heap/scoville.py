# https://school.programmers.co.kr/learn/courses/30/lessons/42626

import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0

    while scoville[0] < K and len(scoville) > 1:
        food1 = heapq.heappop(scoville)
        food2 = heapq.heappop(scoville)

        new_food = food1 + food2 * 2
        heapq.heappush(scoville, new_food)
        cnt += 1

    if scoville[0] < K:
        return -1
    else:
        return cnt


foods = [1, 2, 3, 9, 10, 12]
print(solution(foods, 7))
