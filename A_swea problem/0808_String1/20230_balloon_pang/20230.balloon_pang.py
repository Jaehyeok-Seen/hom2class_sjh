import sys
sys.stdin = open('sample_in.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    
    sum_max_score = 0
    
    for i in range(N):
        for j in range(N):
            center = arr[i][j]
            sum_score = center
            for di,dj in [[-1,0],[1,0],[0,-1],[0,1]]:
                for k in range(1,N):
                    ni,nj = i+di*k, j+dj*k
                    if 0<=ni<N and 0<=nj<N:
                        sum_score += arr[ni][nj]
            if sum_max_score < sum_score:
                sum_max_score = sum_score

    print(f'#{tc} {sum_max_score}')        


