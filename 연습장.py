# for t in range(1, T+1):
#     N = int(input())
#     matrix = [list(map(int, input().split())) for _ in range(N)]

from collections import defaultdict

word_count = defaultdict(int)
word_count['apple'] += 1
print(word_count['apple'])  # 출력: 1

list_dict = defaultdict(list)
list_dict['fruits'].append('apple')
list_dict['fruits'].append('banana')
print(list_dict['fruits'])  # 출력: ['apple', 'banana']

set_dict = defaultdict(set)
set_dict['fruits'].add('apple')
set_dict['fruits'].add('banana')
set_dict['fruits'].add('apple')
print(set_dict['fruits'])  # 출력: {'apple', 'banana'}
