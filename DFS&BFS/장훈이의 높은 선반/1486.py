# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV2b7Yf6ABcBBASw

import sys
sys.stdin = open("input.txt")


def dfs(idx, height, size, shelf):
    global result

    if height >= shelf:
        result = min(result, height)                       # 최솟값 갱신
        return

    if idx == size or height >= result:                    # 종료 조건 & 백트래킹
        return

    dfs(idx + 1, height + heights[idx], size, shelf)       # idx번 점원의 키를 더할까 말까
    dfs(idx + 1, height, size, shelf)

    return


T = int(input())
for t in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    heights.sort()
    result = sum(heights)

    dfs(0, 0, N, B)

    print(f"#{t} {result - B}")
