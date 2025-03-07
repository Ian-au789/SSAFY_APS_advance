# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXO8QBw6Qu4DFAXS

import sys
sys.stdin = open("input.txt")


'''
1. 교차점 발생 조건 (시작점이 Ai보다 높으면 도착점은 Bi보다 낮아야 하고 시작점이 Ai보다 낮으면 도착점은 Bi보다 높아야 한다.)
2. 교차점을 중복 탐색하지 않게 이미 탐색한 전봇대는 또 탐색 대상에 넣지 않는다
'''

T = int(input())
for t in range(1, T+1):
    N = int(input())
    jacks = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0

    for i in range(N - 1):
        start = jacks[i][0]
        end = jacks[i][1]
        for j in range(i + 1, N):
            if jacks[j][0] > start:
                if jacks[j][1] < end:
                    cnt += 1

            else:
                if jacks[j][1] > end:
                    cnt += 1

    print(f"#{t} {cnt}")
