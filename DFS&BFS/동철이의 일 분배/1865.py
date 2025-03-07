# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LuHfqDz8DFAXc

import sys
sys.stdin = open("input.txt")


def dfs(idx, visited, prob, size):
    global result

    if size == idx:
        result = max(result, prob)
        return

    if prob < result:
        return

    for k in range(size):
        if work[idx][k] == 0:
            continue

        else:
            if not visited[k]:
                visited[k] = 1
                dfs(idx + 1, visited, prob * work[idx][k] / 100, size)
                visited[k] = 0
    return


T = int(input())
for t in range(1, T+1):
    N = int(input())
    employees = [i for i in range(N)]
    work = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    dfs(0, [0]*N, 1, N)
    print(f"#{t} {result * 100:.6f}")
