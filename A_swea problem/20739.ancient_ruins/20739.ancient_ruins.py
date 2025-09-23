import sys
sys.stdin = open('sample_in.txt')

def find_max_length(arr,N,M):
    max_length = 0

    #가로 방향
    for i in range(N):  # 각 행마다
        current_length = 0 # 반복돌때마다 카운트를 초기화해야한다.
        for j in range(M): # 열을 돌면서 
            if arr[i][j] == 1:#1인 경우
                current_length +=1#카운트 증가하면서
                max_length = max(max_length,current_length)#맥스 길이 갱신
            else:
                current_length = 0 #만약 1을 못만나면 계속 0으로 갱신
    #세로 방향
    for j in range(M):
        current_length = 0
        for i in range(N):
            if arr[i][j] == 1:
                current_length += 1
                max_length = max(max_length,current_length)
            else:
                current_length = 0
    
    return max_length





pic_data = int(input())

for tc in range(1,pic_data+1):

    N,M = map(int,input().split()) #N x M행렬이다.
    arr = [list(map(int,input().split())) for _ in range(N)]
    

    result = find_max_length(arr,N,M)      
    print(f'#{tc} {result}')      


