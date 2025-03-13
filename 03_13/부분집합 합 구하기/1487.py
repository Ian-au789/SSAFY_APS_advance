import sys
sys.stdin = open("sample_input.txt")


def dfs(subset, size, num, idx):
    global cnt

    if subset == num:
        cnt += 1
        return

    elif subset > num or idx == size:
        return

    else:
        dfs(subset + elements[idx], size, num, idx + 1,)
        dfs(subset, size, num, idx + 1)


T = int(input())
for t in range(1, T+1):
    N, W = map(int, input().split())
    elements = list(map(int, input().split()))
    cnt = 0
    dfs(0, N, W, 0)

    print(f"#{t} {cnt}")
