import sys
sys.stdin = open('5188_input.txt')

def DFS(i,j,current_sum):
    global N, used, min_sum, arr

    if (i,j) == (N-1,N-1):
        min_sum = min(current_sum, min_sum)
        return

    #행렬의 범위를 넘어가도 끝
    if i >= N or j >= N:
        return

    if i < N-1:
        DFS(i+1,j,current_sum + arr[i+1][j])

    if j < N-1:
        DFS(i,j+1,current_sum + arr[i][j+1])




T = int(input())
for tc in range(1,T+1):
    N = int(input())
    min_sum = float('inf')
    arr = [list(map(int,input().split())) for _ in range(N)]
    used = [[False]*(N-1) for _ in range(N)]
    DFS(0,0,arr[0][0])

    print(f'#{tc} {min_sum}')