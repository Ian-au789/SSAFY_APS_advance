# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZVkZjp6DxDHBINE&probBoxId=AZVkSAOaDQPHBINE&type=USER&problemBoxTitle=%2803.19%29++%EA%B7%B8%EB%9E%98%ED%94%841&problemBoxCnt=3

import sys
sys.stdin = open("5247_input.txt")
from collections import deque


def bfs(start, end):
    queue = deque([(start, 0)])

    while 1:
        if queue[0][0] == end:
            return queue[0][1]
        else:
            if queue[0][0] < end and not visited[queue[0][0] + 1]:
                queue.append((queue[0][0] + 1, queue[0][1] + 1))
                visited[queue[0][0] + 1] = 1

            if queue[0][0] - 1 > 0 and not visited[queue[0][0] - 1]:
                queue.append((queue[0][0] - 1, queue[0][1] + 1))
                visited[queue[0][0] - 1] = 1

            if queue[0][0] < end and not visited[queue[0][0] * 2]:
                queue.append((queue[0][0] * 2, queue[0][1] + 1))
                visited[queue[0][0] * 2] = 1

            if queue[0][0] - 10 > 0 and not visited[queue[0][0] - 10]:
                queue.append((queue[0][0] - 10, queue[0][1] + 1))
                visited[queue[0][0] - 10] = 1

            queue.popleft()


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    visited = [0] * 2 * M
    print(f"#{t} {bfs(N, M)}")
