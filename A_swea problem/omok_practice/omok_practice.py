"""
N x N 크기의 판에서
돌이 가로,세로,대각선 중 하나의 방향으로 다섯 개 이상 연속한 부분이 있는지 없는지 판정프로그램
각 문자는 ‘o’또는 ‘.’으로, ‘o’는 돌이 있는 칸을 의미하고, ‘.’는 돌이 없는 칸을 의미한다.
"""

import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1,T+1):

    N = int(input())
    omok_list = [input() for _ in range(N)]
    #===============문제정보 불러오기 완료=============
    result = 'NO'
    delta_i = [1, 1, 0, -1]
    delta_j = [0, 1, 1, 1]

    for i in range(N):
        for j in range(N):
            if omok_list[i][j] == 'o':  # 오목판의 돌을 하나하나 보기위해 이중반복 돌려서 행렬 풀기
                for di,dj in zip(delta_i,delta_j):
                    count = 1
                    for k in range(1,N):

                        ni = i + (di * k)
                        nj = j + (dj * k)


                        if 0 <= ni < N and 0 <= nj < N and omok_list[ni][nj] == 'o':
                            count += 1
                        else:
                            break

                    if count == 5:
                        result = 'YES'




    print(f'#{tc} {result}')



