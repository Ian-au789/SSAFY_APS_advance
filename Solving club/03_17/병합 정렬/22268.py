# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZGv6bK6pRYDFAXd&probBoxId=AZVkSAOaDQHHBINE&type=USER&problemBoxTitle=%2803.17%29++%EB%B6%84%ED%95%A0%EC%A0%95%EB%B3%B5+%EB%B0%8F+%EB%B0%B1%ED%8A%B8%EB%9E%98%ED%82%B91&problemBoxCnt=6

import sys
sys.stdin = open("sample_input(2).txt")


def merge_sort(arr, size):
    global cnt
    mid = size // 2
    left = arr[:mid]
    right = arr[mid:]

    if len(left) > 1:
        left = merge_sort(left, mid)
    if len(right) > 1:
        right = merge_sort(right, size - mid)

    sort_arr = []

    while left and right:
        if left[0] <= right[0]:
            sort_arr.append(left[0])
            left.pop(0)
        else:
            sort_arr.append(right[0])
            right.pop(0)

    if left:
        cnt += 1
        sort_arr.extend(left)
    else:
        sort_arr.extend(right)

    return sort_arr


T = int(input())
for t in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    cnt = 0

    numbers = merge_sort(numbers, N)

    print(f"#{t} {numbers[N // 2]} {cnt}")
