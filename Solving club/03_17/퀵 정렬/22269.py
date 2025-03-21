# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZGv7LIqpSwDFAXd&probBoxId=AZVkSAOaDQHHBINE&type=USER&problemBoxTitle=%2803.17%29++%EB%B6%84%ED%95%A0%EC%A0%95%EB%B3%B5+%EB%B0%8F+%EB%B0%B1%ED%8A%B8%EB%9E%98%ED%82%B91&problemBoxCnt=6

import sys
sys.stdin = open("sample_input(3).txt")


def partition(arr, start, end):
    pivot = arr[start]

    left = start + 1
    right = end

    while 1:
        while left <= end and arr[left] < pivot:
            left += 1
        while start < right and arr[right] > pivot:
            right -= 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            break

    arr[start], arr[right] = arr[right], arr[start]
    return right


def quick_sort(arr, start, end):
    if start < end:
        p = partition(arr, start, end)

        quick_sort(arr, start, p - 1)
        quick_sort(arr, p + 1, end)


T = int(input())
for t in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    quick_sort(numbers, 0, N - 1)

    print(f"#{t} {numbers[N // 2]}")
    print(numbers)
