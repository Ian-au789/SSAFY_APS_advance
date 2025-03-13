# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV15JEKKAM8CFAYD&probBoxId=AZVkSAOaDPvHBINE&type=PROBLEM&problemBoxTitle=%2803.07%29+start+2&problemBoxCnt=4

import sys
sys.stdin = open("sample_input.txt")

'''
1. 암호코드는 8개의 숫자(10진수)로 구성
2. 앞 7자리는 상품의 고유 번호, 마지막 하나는 검증 코드
3. 상품 고유번호의 (홀수 자리의 합 * 3) + 짝수 자리의 합 + 검증 코드 가 10의 배수면 정상적인 암호 코드
4. 16진수로 이루어진 배열에서 2진수로 변환하여 그 안에 있는 암호코드 정보를 확인해야 한다.
5. 한 배열에 암호코드가 1개 이상 있다.
6. 암호화된 암호코드 한 자리의 길이는 최소 7자리고 7의 배수로 늘어난다.
'''


# 암호코드를 해독할 수 있는 사이즈로 변환하는 함수
def resize(input_str, large):
    if large == 1:
        return input_str
    else:
        resized = "".join(map(str, [input_str[i] for i in range(7 * large) if i % large == 0]))
        return resized


T = int(input())
for t in range(1, T+1):
    cypher = {"0001101": 0, "0011001": 1, "0010011": 2, "0111101": 3, "0100011": 4,
              "0110001": 5, "0101111": 6, "0111011": 7, "0110111": 8, "0001011": 9}

    N, M = map(int, input().split())
    matrix = [input() for _ in range(N)]  # 입력값 받기

    hex_code = "007F878787FFF807807F87F87FF8787FFF807F8078007F878007F878"
    # for row in matrix:
    #     for i in range(M):
    #         if row[i] != "0":
    #             hex_code

    bin_code = "0000"
    for h in hex_code:
        h_b = str(bin(int(h, 16))[2:])

        if len(h_b) < 4:
            bin_code += "0" * (4 - len(h_b))

        bin_code += h_b

    N = len(bin_code)
    size = N // 56

    code = []
    idx = 0
    check = 0
    while idx + 7*size < N:
        signal = resize(bin_code[idx:idx + 7 * size], size)
        if signal in cypher and check == 0:  # 암호가 처음 발견되었을 때
            next_signal = resize(bin_code[idx + 7 * size:idx + 2 * 7 * size], size)
            if next_signal in cypher:  # 그 다음 암호도 존재하는 지 확인
                check = 1
                code.append(cypher[signal])  # 해독한 암호 저장
                idx += 7 * size  # 다음 암호 해독 위해 7칸 전진
            else:
                idx += 1

        elif signal in cypher and check == 1:
            code.append(cypher[signal])
            idx += 7 * size

        elif check == 0 and signal not in cypher:  # 암호를 찾을 때 까지 한 칸씩 전진
            if len(code) > 0:
                break
            else:
                idx += 1

        else:  # 해독 완료하면 break
            break

    odd = sum([code[i] for i in range(len(code)) if i % 2 == 0])  # 홀수 자리의 합
    even = sum([code[i] for i in range(len(code)) if i % 2 == 1])  # 짝수 자리의 합

    # 올바른 암호면 해독 결과 출력, 그렇지 않으면 0 출력
    if (odd * 3 + even) % 10 == 0:
        result = sum(code)

    else:
        result = 0

    print(f"#{t} {result}")

