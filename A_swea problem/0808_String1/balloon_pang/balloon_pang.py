# M x N 배열에 풍선이 붙어있고
# 어떤 풍선을 터뜨릴 경우 안에 든 종이 꽃가루 수만큼 상하 좌우의 풍선이 추가로 터지는 게임
# (기준포인트의 값을 바탕으로 추가 풍선 터뜨리기)
#
# 이때 꽃가루 개수 A가 주어지면, 한 개의 풍선을 선택했을 때 날릴 수 있는 꽃가루의 합 중 최대값을 출력
# (3<= N, M <= 100)

import sys
sys.stdin = open ( 'input1.txt')

T = int(input())
for tc in range(1,T+1):
    N,M = tuple(map(int,input().split()))
    arr = [list(map(int,input().split())) for _ in range(N)]


    max_sum_pang = 0 # 최종적으로 구해야하는 풍선 터지는 수의 합
    for i in range(N):
        for j in range(M):
            point = arr[i][j]
            sum_pang = point
            for di, dj in [[-1,0],[1,0],[0,-1],[0,1]]:
                for k in range(1, point+1):
                    ni, nj = i + di*k, j + dj*k # 기준 풍선의 꽃가루 수만큼 더 터뜨려야하니까 곱해줌
                    if 0 <= ni < N and 0 <= nj < M: #범위 제한두는 코드 작성완료
                        sum_pang += arr[ni][nj]
            if max_sum_pang < sum_pang:
                max_sum_pang = sum_pang
    print(f'#{tc} {max_sum_pang}')
