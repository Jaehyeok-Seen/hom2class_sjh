import sys
sys.stdin = open('input.txt')
# 사다리 기본 원리 해당열에 [x][1] 을 따라 끝범위까지 가는 기본 루트에 
# 조건: 델타탐색으로 좌우에 1을 발견하게 되면 기본루트 멈추고 좌우 1을 따라 이동(단 좌 우의 값이 1이 아니게 될때까지 이동)
# 조건2: 만약 이동이 끝나고 나면 무조건 아래로 한칸 이동
# 조건3: 마지막 100행에서의 값이 2가 되는 사다리를 발견하면 종료하고 그 사다리의 출발점 x좌표를 출력
# 좌우 이동이 배열범위 바깥을 넘어가지 않도록 and이용해서 제한
# 사다리의 개수 파악 (행[0][y]의 값이 1인 경우를 모두 탐색하면됨)

def ladder_search(goal, ladder_arr):
    #시작점을 입력하면 목표지점의 좌표값을 찾아주는 함수
    x=99
    y= goal  # ladder_arr[99][goal]에서 부터 역으로 올라가는 함수 

    while x>0 :
        x -= 1 #0이 마지막 경계지점,이 닿을 때까지 x의 좌표를 하나씩 줄여서간다.

        if y>0 and ladder_arr[x][y-1] ==1:  #왼쪽에서 1값을 찾을 때 
            while y>0 and ladder_arr[x][y-1] == 1:
                y-=1 #좌측으로 1이 끝날때까지 이동
        elif y<99 and ladder_arr[x][y+1] ==1:
            while y< 99 and ladder_arr[x][y+1] == 1:
                y+=1 #우측으로 1이 끝날때가지 이동
    return y


for tc in range(1,11):
    tc = int(input())
    ladder_arr = [list(map(int,input().split())) for _ in range(100)]
    #print(ladder) 리스트 안에 100개씩 잘 들어감

    start = 0 # 어차피 골은 x=0의 좌표로 고정

    for y in range(100):
        if ladder_arr[99][y] ==2 : 
            start = y
    
    result = ladder_search(start, ladder_arr)
    print(f'#{tc} {result}')
            
































# 처음 시도한 버전    
    # ladder_column = [] #사다리의 시작'열' 좌표값 
    # for j in range(100):
    #     if ladder[0][j] == 1:
    #         ladder_column.append(j)
    # # print(ladder_column) 
    # ladder_count = len(ladder_column)  #사다리의 개수
    # # print(ladder_count)
    

    # # 기본 사다리 타기 로직 만들기
    # for j in ladder_column: # 사다리 열 값을 반복하고
    #     for i in range(100): # 각각의 사다리 열에서 행을 100까지 반복
    #         explore_point = [i,j]
    #         for di,dj in [[0,-1],[0,1]]:
    #             ni,nj = i+di,i+dj
    #             if 0<= ni < 100 and 0 <= nj < 100 and ladder[ni][nj]==1:
    #                 while ladder[ni][nj] != 0:
    #                     explore_point = [i,j+1]


            

# def delta_function():
#     #기준점 잡고
#     point = [i, j]
#     for di,dj in [[0,-1],[0,1]]:
#         [ni,nj] = [i+di, j+dj]
#         if 0<= ni < 100 and 0 <= nj < 100:
#             new_point = ladder[ni][nj]
#             if new_point == 0:
#                 pass
#             elif new_point == 1:
#                 point = [i,j+1]
#                 if new_point == 0:
#                     point = [i,j]


