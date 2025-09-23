# # ;  조망권 = 현재 빌딩 높이 
# # ;  max(좌측 2칸 ~ 우측 2칸)을 찾아서
# # ;  조망권 = 현재빌딩 높이 - max(좌측 2칸 ~ 우측 2칸)
# # ;  코드로 진입하기 전에는 
# # ;  문제를 완독하고 가야 위에서 바로 코딩갈때에 놓칠만한 부분들을 조심할 수 있다.

# # ;  문제 제한사항에 보면 
# # ;  - 가로 길이는 1000이하
# # ;  - 맨 왼쪽 두칸과 오른쪽 두칸에는 건물이 지어지지 않는다
# # ;  - 각 빌딩의 높이는 최대 255이다.

# import sys
# sys.stdin = open('sample_input.txt')

# T = 10
# for tc in range(1, T+1):
#   # N: 건물의 갯수 (4 <= N <= 1000)
#   # N개의 건물의 높이가 주어진다.
#     N = int(input())
#     building_list = list(map(int, input().split())) #integer로 형변환

#     print(N,building_list)
#     # 전체 조망권의 갯수를 구하는 것이 목표! 
#     # 조망권을 누적해서 구해야한다.
#     # 좌측 2 ~ 우 2 빌딩이 현재 빌딩보다 낮다면, 아래에 있는 계산을 하면 된다.
#     # 조망권 = 현재 빌딩의 높이 - max(좌2, 좌1, 우1, 우2) 중 가장 높은 빌딩을 빼주면된다.
#     total_good_view = 0
#     for idx in range(2, N-2):   # idx :  현재 빌딩
#         # 빌딩이 없는 경우 스킵
#         if building_list[idx] == 0 :
#             continue # 다음 빌딩으로

#     curr = building_list[idx] # 현재 빌딩 높이 
#     left2 = building_list[idx-2] # 좌측 2칸
#     left1 = building_list[idx-1] # 좌측 1칸
#     right1 = building_list[idx+1] # 우측 1칸
#     right2 = building_list[idx+2] # 우측 2칸

#     highest_near_building = 0
#    #조망권이 존재하는지 여부 확인
#     if(curr > left2) and (curr > left1) and (curr> right1) and (curr > right2):
#         if highest_near_building < left2:
#             highest_near_building = left2
    
#         if highest_near_building < left1:
#             highest_near_building = left1

#         if highest_near_building < right1:
#             highest_near_building = right1

#         if highest_near_building < right2:
#             highest_near_building = right2
#     #하나만 비교하는게 아닌 전부 다 비교해야하기 때문에 elif 쓰면 무조건 lef2로만 바뀐다.
#     # print(highest_near_building)
#     good_view = curr - highest_near_building
#     total_good_view += good_view
#     # 모든 빌딩에 대해 반복
    
#     print(f'#{tc} {total_good_view}')



import sys
sys.stdin = open('sample_input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    building_list = list(map(int, input().split()))

    total_good_view = 0
    for idx in range(2, N-2):
        if building_list[idx] == 0:
            continue

        curr = building_list[idx]
        left2 = building_list[idx-2]
        left1 = building_list[idx-1]
        right1 = building_list[idx+1]
        right2 = building_list[idx+2]

        if (curr > left2) and (curr > left1) and (curr > right1) and (curr > right2):
            highest_near_building = 0
            if highest_near_building < left2:
                highest_near_building = left2
        
            if highest_near_building < left1:
                highest_near_building = left1

            if highest_near_building < right1:
                highest_near_building = right1

            if highest_near_building < right2:
                highest_near_building = right2

            good_view = curr - highest_near_building
            total_good_view += good_view
    
    print(f'#{tc} {total_good_view}')