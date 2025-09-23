import sys
sys.stdin = open('input.txt')

    
T = int(input())

for tc in range(1, T+1):

    N,M = map(int,input().split())   # NxN 크기의 배열에서 MxM의 파리채
    arr = [list(map(int,input().split()))for _ in range(N)]  #파리의 수가 적힌 행렬
    # 5<=N<=15
    # M<=2<=N
    max_kill = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            # print(f'위치 ({i},{j}): ', end="")      #디버깅을 대신할 프린트 기억해두기
            point = arr[i][j]  # 0,0에서 부터 시작
            
            kill_sum = 0    #파리채로 죽인 파리수 합
            for di in range(M):
                for dj in range(M):
                    ni,nj = i+di, j+dj

                    # if 0<= ni < N and 0<= nj < M:
                    kill_sum += arr[ni][nj]
                    if max_kill < kill_sum:
                        max_kill = kill_sum

            # print(f"={kill_sum}")
    print(f'#{tc} {max_kill}')
