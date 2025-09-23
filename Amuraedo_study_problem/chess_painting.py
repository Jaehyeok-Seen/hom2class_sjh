"""
시작이 W인 경우
시작이 B인 경우
두개 비교
시작범위부터 8개 체스판 늘릴때 범위 넘어가지 않게 설정

"""
chess_W = [
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ]

chess_B = [
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ]

M, N = map(int,input().split())
# M = 행
# N = 열
board = [ list(input()) for _ in range(M) ]
min_result = float('inf')
#board에서 체스판 완전 검색 돌리기
#그러기 위해 시작점 위치 탐색 돌리기 먼저
for start_i in range(M-7): #범위의 경우 8칸 체스판했을 때 범위 넘어가지 않게
    for start_j in range(N-7):

        count_W = 0
        for i in range(8):
            for j in range(8):
                if board[start_i+i][start_j+j] != chess_W[i][j]:
                    count_W += 1

        count_B = 0
        for i in range(8):
            for j in range(8):
                if board[start_i+i][start_j+j] != chess_B[i][j]:
                    count_B += 1
        min_result = min(min_result,count_W,count_B)

print(min_result)