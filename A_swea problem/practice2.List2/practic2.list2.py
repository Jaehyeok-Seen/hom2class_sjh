"""
5x5 2차 배열에서 25개의 숫자 초기화
반복돌리는 과정 중에 한 값을 기준으로 |인접한 값-기준값|의 합을 결과값을 가지면 된다.
절대값은 abs(-1)이렇게 쓴다.
- 제한사항 
벽에 있는 친구들은 요소가 2개일 수 있다. 범위 조심
"""
import sys
sys.stdin = open('ex1_input.txt')

T = int(input()) #테스트 케이스 

for indx1 in range(1,T+1):
    N = int(input()) #N x N 크기 지정
    arr_list = []
    for indx2 in range(5):
        arr = list(map(int,input().split()))
        arr_list.append(arr)
    
    sum_difference = 0 # 이 총합 변수 위치를 어떻게 두는냐에 따라 값이 바뀌니까 중요함
                       # 지금처럼 총합이라고 하면 i보다 바깥, 행마다 값을 구해야하면 i안쪽, 개별 합계구하려면 j안쪽

    for i in range(N):

        for j in range(N): #주어진 arr_list 반복돌리면서 기준값의 상하좌우 값들과의 차를 구해야한다.
             #구해야하는 절댓값 차의 합계
            
            for di,dj in [[-1,0],[1,0],[0,-1],[0,1]]: #델타 이용해서 상하좌우 범위 설정완료
                ni,nj = i+di, j+dj #인접한 값들 구했으니 여기서 각각 기준값을 설정하고 빼야함
                
                if 0<=ni <N and 0<=nj <N:
                    sum_difference += abs(arr_list[i][j] - arr_list[ni][nj])

    print(f'#{indx1} {sum_difference}')
       
            
                
    
    



# A='45 15 10 56 23'
# A_arr= list(map(int,A.split()))
# print(A_arr)

'''

총합을 구한게 아니라 배열을 만드는걸로 착가한 코드 나중에 다시 해보기
import sys
sys.stdin = open('ex1_input.txt')

T = int(input()) #테스트 케이스 

for indx1 in range(1,T+1):
    N = int(input()) #N x N 크기 지정
    arr_list = []
    for indx2 in range(5):
        arr = list(map(int,input().split()))
        arr_list.append(arr)
    
    for i in range(N):
        for j in range(N): #주어진 arr_list 반복돌리면서 기준값의 상하좌우 값들과의 차를 구해야한다.
            sum_difference = 0  #구해야하는 절댓값 차의 합계
            for di,dj in [[-1,0],[1,0],[0,-1],[0,1]]: #델타 이용해서 상하좌우 범위 설정완료
                ni,nj = i+di, j+dj #인접한 값들 구했으니 여기서 각각 기준값을 설정하고 빼야함
                center = arr_list[i][j]

                for num in range(4):
                    difference = arr[ni][nj] - center
                    abs_difference = abs(difference)
                    sum_difference += abs_difference
            
            if 0<=ni <N and 0<=nj <N:
    
'''