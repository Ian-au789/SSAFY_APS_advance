# for t in range(1, T+1):
#     N = int(input())
#     matrix = [list(map(int, input().split())) for _ in range(N)]

from itertools import permutations

areas = [1, 2, 3, 4, 5]
print(list(permutations(areas)))
