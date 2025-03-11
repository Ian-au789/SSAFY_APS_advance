# 우선순위 큐를 구현하는 가장 효율적인 방법은 힙(heap)
# heapq 라이브러리를 써서 최소 힙 구현

import heapq

# 빈 우선순위 큐 생성
priority_queue = []

# 우선순위를 가진 항목들 삽입
heapq.heappush(priority_queue, (3, "3 priority task"))
heapq.heappush(priority_queue, (1, "1 priority task"))
heapq.heappush(priority_queue, (2, "2 priority task"))

# 우선순위가 큰 요소부터 하나씩 꺼내 출력 (heapq 는 최소힙을 구현하므로 숫자가 작은 것 부터)
while priority_queue:
    task = heapq.heappop(priority_queue)
    print(task)
