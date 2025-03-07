# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AY4XhKTKU0IDFARM

import sys
sys.stdin = open("sample_input.txt")

'''
1. 세 번째 상자가 2 이하의 사탕을 가지면 불가능
2. 2번째 상자가 3번째 상자보다 1개 적도록 사탕을 먹는다. 그 다음도 동일
'''


def candy(a, b, c):
    if c < 3 or b == 1:
        return -1

    elif a < b < c:
        return 0

    else:
        eat = 0

        if b >= c:
            eat += b - c + 1
            b = c - 1

        if a >= b:
            eat += a - b + 1

    return eat


T = int(input())
for t in range(1, T+1):
    A, B, C = map(int, input().split())

    print(f"#{t} {candy(A, B, C)}")
