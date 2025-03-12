# https://swexpertacademy.com/main/talk/solvingClub/problemBoxDetail.do?solveclubId=AZTP1QzqXnbHBIRD&probBoxId=AZVkSAOaDP7HBINE

import sys
sys.stdin = open("input.txt")


def short_cut(ci, cj, size, path, left):
    global result

    if left == 0:
        path += abs(house[0] - ci) + abs(house[1] - cj)

        if path < result:
            result = path
        return

    if path > result:
        return

    for i in range(size):
        if not visited[i]:
            visited[i] = 1
            short_cut(customers[i][0], customers[i][1], size,
                      path + abs(customers[i][0] - ci) + abs(customers[i][1] - cj), left - 1)
            visited[i] = 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    cor = list(map(int, input().split()))

    company = [cor[0], cor[1]]
    house = [cor[2], cor[3]]
    customers = [[cor[2*i], cor[2*i+1]] for i in range(N + 2) if i > 1]
    visited = [0]*N

    result = 1000
    short_cut(company[0], company[1], N, 0, N)

    print(f"#{t} {result}")
