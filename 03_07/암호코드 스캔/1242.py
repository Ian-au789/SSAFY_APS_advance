# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV15JEKKAM8CFAYD&probBoxId=AZVkSAOaDPvHBINE&type=PROBLEM&problemBoxTitle=%2803.07%29+start+2&problemBoxCnt=4

import sys
sys.stdin = open("sample_input.txt")


T = int(input())

cypher = {"0001101": 0, "0011001": 1, "0010011": 2, "0111101": 3, "0100011": 4,
          "0110001": 5, "0101111": 6, "0111011": 7, "0110111": 8, "0001011": 9}