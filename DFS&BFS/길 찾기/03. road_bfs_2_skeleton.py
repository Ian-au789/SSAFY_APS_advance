import sys
sys.stdin = open('practice_input.txt')

def get_road_move_time(road, n, m):
    pass

# 도로의 크기 n * m 입력 받기
n, m = map(int, input().split())
road = [list(map(int, input())) for _ in range(n)]  # 도로 정보 입력

result = get_road_move_time(road, n, m)  # BFS를 이용해서 이동시간 구하기
print(result)
