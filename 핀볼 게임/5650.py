# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AWXRF8s6ezEDFAUo&probBoxId=AZTeuPGad_vHBIOK&type=PROBLEM&problemBoxTitle=A%ED%98%95+%EC%97%AD%EB%9F%89%ED%85%8C%EC%8A%A4%ED%8A%B8+%EB%AA%A8%EC%9D%8C%EC%A7%91+&problemBoxCnt=20

import sys
sys.stdin = open("sample_input.txt")


def pinball():
    pass


T = int(input())
for t in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    empty = []
    blocks = {}
    worm_hole = {}
    black_hole = set()

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                blocks[1] = (i, j)

            elif matrix[i][j] == 2:
                blocks[2] = (i, j)

            elif matrix[i][j] == 3:
                blocks[3] = (i, j)

            elif matrix[i][j] == 4:
                blocks[4] = (i, j)

            elif matrix[i][j] == 5:
                blocks[5] = (i, j)

            elif matrix[i][j] == 6:
                worm_hole[6] = (i, j)

            elif matrix[i][j] == 7:
                worm_hole[7] = (i, j)

            elif matrix[i][j] == 8:
                worm_hole[8] = (i, j)

            elif matrix[i][j] == 9:
                worm_hole[9] = (i, j)

            elif matrix[i][j] == 10:
                worm_hole[10] = (i, j)

            elif matrix[i][j] == -1:
                black_hole.add((i, j))

            else:
                empty.append((i, j))

    print(empty)
    print(blocks)
    print(worm_hole)
    print(black_hole)

    # print(f"#{t} {}")
