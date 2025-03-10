# 파스칼의 삼각형처럼 이항계수를 구하지만 DP를 이용해라

def binomial_coefficient(n, k):
    bc = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(i+1):
            if j == 0 or j == i:
                bc[i][j] = 1

            else:
                bc[i][j] = bc[i-1][j-1] + bc[i-1][j]

    return bc[n][k]


print(binomial_coefficient(25, 17))
