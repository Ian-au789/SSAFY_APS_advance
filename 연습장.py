# for t in range(1, T+1):
#     N = int(input())
#     matrix = [list(map(int, input().split())) for _ in range(N)]

dict = {1: 2, 3: 4}
i = 1
while dict:
    print(dict.pop(i))
    i += 2
print(dict)

print(list(range(-10, 11)))