import sys
sys.stdin = open("sample_input(2).txt")


def merge_sort(arr):
    n = len(arr)

    if n <= 1:
        return arr

    mid = n // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    global cnt
    result = []

    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if left:
        cnt += 1
        result.extend(left)
    else:
        result.extend(right)

    return result


T = int(input())
for t in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    cnt = 0

    numbers = merge_sort(numbers)

    print(f"#{t} {numbers[N // 2]} {cnt}")
