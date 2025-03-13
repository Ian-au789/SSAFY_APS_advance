import sys
sys.stdin = open("sample_input.txt")


T = int(input())
for t in range(1, T+1):
    N, W = map(int, input().split())
    elements = list(map(int, input().split()))
    dp = [-1] * (1 << N)



    print(f"#{t} {}")