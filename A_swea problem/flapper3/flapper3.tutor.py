import sys
sys.stdin = open('in1.txt')

T = int(input())
for tc in range(1, T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    Max_kill  = 0 # 구해야할 최대 파리 죽인 수 (영향받지 않는 위치에서 선언)

    plus_dir = [[-1,0],[1,0],[0,-1],[0,1]] #플러스 모양과 x모양일때 
    x_dir = [[-1,-1],[-1,1],[1,-1][1,1]] #델타방향들을 미리 변수에 할당

    for i in range(N):
        for j in range(N): #arr을 하나씩 다 푸는 for문 작성
            point = arr[i][j]

            plus_sum = point
            x_sum = point

            for move in range(1,M): # 중심점이 포함되지 않게 하기 위해 1부터
            # plus_sum 부터 정의 시작
                for di,dj in plus_dir: #미리 정의해둔 방향으로 델타 검색
                    ni = i + di*move    #move만큼 이동 부분까지 고려
                    nj = i + dj*move
                    if 0<=ni<N and 0<=nj<N:
                        plus_sum += arr[i][j]
            # x_dir 도 정의 시작   
                for di,dj in x_dir:
                    ni = i + dj*move
                    nj = i + dj*move
                    if 0<=ni<N and 0<=nj<N:
                        x_sum += arr[i][j]

            if Max_kill < plus_sum:
                Max_kill = plus_sum
            if Max_kill < x_sum:
                Max_kill = x_sum
    
    print(f'#{tc} {Max_kill}')




