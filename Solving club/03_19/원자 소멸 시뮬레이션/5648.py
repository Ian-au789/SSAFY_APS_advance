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
            if cur_loc in already:     # 이미 소멸된 원자는 제거
                continue

            # 다음 위치 계산
            next_loc = (cur_loc[0] + direction[atoms[cur_loc][0][0]][0],
                        cur_loc[1] + direction[atoms[cur_loc][0][0]][1])

            if next_loc[0] not in range(-1000, 1001) or \
                    next_loc[1] not in range(-1000, 1001):   # 범위 밖을 벗어나면 제거
                continue

            # 이 원자의 다음 위치가 현재 다른 원자의 위치와 겹치는 지 확인
            if next_loc in atoms:
                if (atoms[cur_loc][0][0] + atoms[next_loc][0][0]) % 4 == 1:   # 충돌 발생
                    energy += atoms[cur_loc][0][1]
                    energy += atoms[next_loc][0][1]
                    already.add(next_loc)          # 아직 다음 위치를 계산하지 않았지만 이미 소멸된 원자의 현재 위치 저장
                    continue

            # 이 원자의 다음 위치에 이미 원자가 존재하는 경우
            if next_loc in new_atoms:
                new_atoms[next_loc].append(atoms[cur_loc][0])     # 딕셔너리의 키 값에 원자 저장
                collide.add(next_loc)                             # 충돌이 일어난 위치라고 표시
            else:
                new_atoms[next_loc] = atoms[cur_loc]              # 아무 일도 안 일어난 원자는 새로운 딕셔너리에 저장

        # 충돌 시 에너지 방출
        if len(collide) > 0:
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
        atom_dict[(atom[0], atom[1])] = [(atom[2], atom[3])]         # (x 좌표, y좌표) : (방향, 에너지) 형태로 저장

    direction = {0: (0, 1), 1: (0, -1), 2: (-1, 0), 3: (1, 0)}       # 원자 진행 방향
    print(f"#{t} {nuclear_reaction(atom_dict)}")
