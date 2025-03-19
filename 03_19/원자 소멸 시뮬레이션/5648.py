# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AWXRFInKex8DFAUo&probBoxId=AZTeuPGad_vHBIOK&type=PROBLEM&problemBoxTitle=A%ED%98%95+%EC%97%AD%EB%9F%89%ED%85%8C%EC%8A%A4%ED%8A%B8+%EB%AA%A8%EC%9D%8C%EC%A7%91+&problemBoxCnt=20

import sys
sys.stdin = open("sample_input.txt")

'''
1. 원자들 다음에 이동할 위치 계산
2. 이동하기 전에 한 칸 간격으로 서로 마주보고 있는 원자가 있다면 에너지 방출
3. 이동 후 같은 칸에 존재하는 원자가 있다면 에너지 방출
4. 에너지가 방출된 원자는 리스트에서 삭제, 범위 밖을 벗어난 원자도 삭제
'''


def nuclear_reaction(atoms):
    energy = 0
    size = len(atoms)

    while size > 0:
        cur_loc = []
        next_loc = []
        # 현재 위치, 다음 위치 저장
        for atom in atoms:
            if atom[0] in range(-1000, 1001) and atom[1] in range(-1000, 1001):  # 범위을 벗어나면 제거
                cur_loc.append([atom[0], atom[1]])
                next_loc.append([atom[0] + direction[atom[2]][0], atom[1] + direction[atom[2]][1]])
            else:
                size -= 1

        collide = set()

        # 충돌 확인
        for i in range(size):
            for j in range(i + 1, size):
                if next_loc[i] == cur_loc[j]:
                    if (atoms[i][2] + atoms[j][2]) % 4 == 1:
                        collide.add(i)
                        collide.add(j)

                if next_loc[i] == next_loc[j]:
                    collide.add(i)
                    collide.add(j)

        new_atoms = []
        for k in range(size):
            if k in collide:
                energy += atoms[k][3]

            else:
                new_atoms.append([next_loc[k][0], next_loc[k][1], atoms[k][2], atoms[k][3]])

        if len(new_atoms) > 0:
            atoms = [row[:] for row in new_atoms]
            size = len(atoms)
        else:
            break

    return energy


T = int(input())
for t in range(1, T+1):
    N = int(input())
    atom_list = [list(map(int, input().split())) for _ in range(N)]
    direction = {0: (0, 1), 1: (0, -1), 2: (-1, 0), 3: (1, 0)}

    print(f"#{t} {nuclear_reaction(atom_list)}")
