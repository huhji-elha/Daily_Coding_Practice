# 브루트 포스 - 체스판 다시 칠하기
import sys
import copy 
N, M = map(int, sys.stdin.readline().split())
_chess_list = []

for m in range(N):
    _chess_list.append(list(sys.stdin.readline())[:M])

def get_tile_differ(N, M, chess_list, start_black=False):
    _pattern_w = ['W', 'B']
    _pattern_b = ['B', 'W']
    
    _longer = max(N,M)
    _pattern_1 = _pattern_w*(_longer//2+1)
    _pattern_2 = _pattern_b*(_longer//2+1)
    
    if start_black:
        _pattern_1, _pattern_2 = _pattern_2, _pattern_1
    for i, width in enumerate(chess_list):
        if i%2 == 0:
            _pattern = _pattern_1
        else:
            _pattern = _pattern_2
        for j in range(M):
            if width[j] == _pattern[j]:
                width[j] = 0
            else:
                width[j] = 1
    return chess_list

_chess_list_b = copy.deepcopy(_chess_list)

_chess_list_w = get_tile_differ(N,M,_chess_list)
_chess_list_b = get_tile_differ(N,M,_chess_list_b, start_black=True)


_sum_list = []
for _list in [_chess_list_w, _chess_list_b]:
    i,j = 0,0
    for j in range(0, M-8+1):
        for i in range(0, N-8+1):
            _sum = 0
            for width in _list[i:i+8]:
                _sum += sum(width[j:j+8])
            _sum_list.append(_sum)

print(min(_sum_list))