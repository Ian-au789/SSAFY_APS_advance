# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV7I5fgqEogDFAXB&probBoxId=AZVkSAOaDQLHBINE&type=PROBLEM&problemBoxTitle=%2803.18%29++%EB%B6%84%ED%95%A0%EC%A0%95%EB%B3%B5+%EB%B0%8F+%EB%B0%B1%ED%8A%B8%EB%9E%98%ED%82%B92&problemBoxCnt=5

import sys
sys.stdin = open("sample_input.txt")


def dfs(ci, cj, level, num_list):
    if level == 7:
        result = "".join(map(str, num_list))   # 앞자리 0 유지하도록 문자열 사용
        numbers.add(result)
        return

    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    for k in range(4):
        ni = ci + di[k]
        nj = cj + dj[k]

        if 0 <= ni < 4 and 0 <= nj < 4:   # 범위 한정
            num_list.append(matrix[ni][nj])
            dfs(ni, nj, level + 1, num_list)
            num_list.pop()


T = int(input())
for t in range(1, T+1):
    matrix = [list(map(int, input().split())) for _ in range(4)]
    numbers = set()       # 중복 제거용 set 사용

    for i in range(4):
        for j in range(4):
            dfs(i, j, 1, [matrix[i][j]])

    print(f"#{t} {len(numbers)}")
