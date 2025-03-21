# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AXAdtcu61xwDFAXq&probBoxId=AZVkSAOaDQXHBINE&type=PROBLEM&problemBoxTitle=%2803.21%29++%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B43&problemBoxCnt=6

import sys
sys.stdin = open("sample_input.txt")


def switch(k):         # 스위치 눌러서 전구 끄거나 켜기
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if i == k or j == k:
                matrix[i][j] = (matrix[i][j] + 1) % 2


T = int(input())
for t in range(1, T+1):
    n = int(input())
    m = int(input())
    matrix = [[1]*n for _ in range(n)]        # 선형 전구의 켜짐/꺼짐 상태를 행렬로 표현

    for i in range(n):                        # 자기 자신과 연결된 선형 전구는 없음
        for j in range(n):
            if i == j:
                matrix[i][j] = 0

    for _ in range(m):
        a, b = map(int, input().split())      # 초기 상태
        matrix[a-1][b-1] = 0
        matrix[b-1][a-1] = 0

    last = -1
    while 1:
        turned_on = [0]*n
        top = 0

        # 가장 많은 전구를 끌 수 있는 스위치를 찾아서 누르는 탐욕 방식
        for idx in range(n):
            turned_on[idx] = sum(matrix[idx])
            if turned_on[idx] > turned_on[top]:
                top = idx

        if sum(turned_on) == 0:   # 모든 전구가 꺼졌으면 종료
            c = 0
            break
        else:
            if top == last:    # 만약 직전에 눌렀던 스위치를 또 누른다면 무한루프에 빠지고 모든 전구를 끌 수 없다.
                c = 1
                break

            last = top
            switch(top)

    check = {0: "DA", 1: "NE"}
    print(f"#{t} {check[c]}")
