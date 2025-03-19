# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AWXRFInKex8DFAUo&probBoxId=AZTeuPGad_vHBIOK&type=PROBLEM&problemBoxTitle=A%ED%98%95+%EC%97%AD%EB%9F%89%ED%85%8C%EC%8A%A4%ED%8A%B8+%EB%AA%A8%EC%9D%8C%EC%A7%91+&problemBoxCnt=20

import sys
sys.stdin = open("sample_input.txt")


def nuclear_reaction(atoms):
    energy = 0

    while atoms:
        new_atoms = {}
        collide = set()
        already = set()
        for cur_loc in atoms:
            if cur_loc in already:
                continue

            next_loc = (cur_loc[0] + direction[atoms[cur_loc][0][0]][0], cur_loc[1] + direction[atoms[cur_loc][0][0]][1])

            if next_loc[0] not in range(-1000, 1001) or next_loc[1] not in range(-1000, 1001):  # 범위 밖을 벗어나면 제거
                continue

            if next_loc in atoms:
                if (atoms[cur_loc][0][0] + atoms[next_loc][0][0]) % 4 == 1:   # .5초 충돌 발생
                    energy += atoms[cur_loc][0][1]
                    energy += atoms[next_loc][0][1]
                    already.add(next_loc)
                    continue

            if next_loc in new_atoms:
                new_atoms[next_loc].append(atoms[cur_loc][0])          # 충돌 발생
                collide.add(next_loc)
            else:
                new_atoms[next_loc] = atoms[cur_loc]

        if len(collide) > 0:           # 충돌 시 에너지 방출
            for c in collide:
                nuc = new_atoms.pop(c)
                for n in nuc:
                    energy += n[1]

        atoms = new_atoms

    return energy


T = int(input())
for t in range(1, T+1):
    N = int(input())
    atom_list = [list(map(int, input().split())) for _ in range(N)]
    atom_dict = {}
    for atom in atom_list:
        atom_dict[(atom[0], atom[1])] = [(atom[2], atom[3])]

    direction = {0: (0, 1), 1: (0, -1), 2: (-1, 0), 3: (1, 0)}
    print(f"#{t} {nuclear_reaction(atom_dict)}")
