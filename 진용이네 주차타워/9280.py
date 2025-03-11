# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AW9j74FacD0DFAUY

import sys
sys.stdin = open("sample_input.txt")


def guests_done(size):
    profit = 0
    parking_lot = [0] * size
    waiting_list = []

    while len(car_move) > 0:
        idx = 0

        if car_move[0] > 0:
            while parking_lot[idx] and idx < size:
                idx += 1

                if idx == size:
                    break

            if idx < size:
                parking_lot[idx] = car_move[0]

            else:
                waiting_list.append(car_move[0])

        else:
            num = -1 * car_move[0]

            while parking_lot[idx] != num:
                idx += 1

            profit += car_weight[num - 1] * parking_fee[idx]
            parking_lot[idx] = 0

            if len(waiting_list) > 0:
                parking_lot[idx] = waiting_list[0]
                waiting_list.pop(0)

        car_move.pop(0)

    return profit


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    parking_fee = []
    for _ in range(N):
        parking_fee.append(int(input()))

    car_weight = []
    for _ in range(M):
        car_weight.append(int(input()))

    car_move = []
    for _ in range(2*M):
        car_move.append(int(input()))

    print(f"#{t} {guests_done(N)}")
