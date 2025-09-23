import sys
sys.stdin = open('5188_input.txt')

def moving(current_sum,i,j):
    global min_sum, arr
    #기저조건 먼저 생각하기
    if i == N-1 and j ==N-1:    # 도착점에 도달하면 끝
        min_sum = min(min_sum,current_sum)

        return

    if i >= N or j >= N:
        return

    if i < N-1:
        moving(current_sum+arr[i+1][j],i+1,j)

    if j < N-1:
        moving(current_sum+arr[i][j+1],i,j+1)

T=int(input())
for tc in range(1,T+1):
    N= int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    min_sum = float('inf')
    moving(arr[0][0],0,0)


    print(min_sum)

