import sys
sys.stdin = open('in1.txt')

T = int(input())
for tc in range(1, T+1):
    N,M = tuple(map(int,input().split())) #파리 위치 행렬의 크기
    arr = [list(map(int,input().split())) for _ in range(N)] #파리 위치

    Max_kill = 0 # 우리가 알아야 할 죽인 파리수의 최댓값(영향을 최대한 안받아야 함)

    for i in range(N):
        for j in range(N):
            point = arr[i][j]
            plus_sum = point
            X_sum = point

            for k in range(1,M): #기준으로 뻗어나가는데 그 범위를 지정
                
                #플러스 모양으로 나오는 경우
                for di, dj in [[-1,0],[1,0],[0,-1],[0,1]]:
                    ni,nj = i+di*k, j+dj*k
                    if 0<= ni < N and 0<= nj < N:
                        plus_sum += arr[ni][nj]
                        

                #X 모양으로 나오는 경우
                for di, dj in [[-1,-1],[1,-1],[1,-1],[1,1]]:
                    ni,nj = i+di*k, j+dj*k
                    if 0<= ni < N and 0<= nj < N:
                        X_sum += arr[ni][nj]

            if Max_kill < plus_sum:
                Max_kill = plus_sum
            elif Max_kill < X_sum:
                Max_kill = X_sum

    print(f'#{tc} {Max_kill}')
            #X자 모양으로 나오는 경우


