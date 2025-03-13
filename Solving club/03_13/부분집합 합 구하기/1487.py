import sys
sys.stdin = open("sample_input.txt")


def dfs(subset, size, num, idx):
    global cnt

    if subset == num:        # 원하는 부분합에 도달하면 카운트
        cnt += 1
        return

    elif subset > num or idx == size:        # 원하는 부분합을 넘거나 모든 원소를 탐색했으면 중지
        return

    else:
        dfs(subset + elements[idx], size, num, idx + 1,)     # 해당 원소를 더할까 말까
        dfs(subset, size, num, idx + 1)


T = int(input())
for t in range(1, T+1):
    N, W = map(int, input().split())
    elements = list(map(int, input().split()))
    cnt = 0
    dfs(0, N, W, 0)

    print(f"#{t} {cnt}")
