import sys
sys.stdin = open('sample_input.txt')

# 제한 사항 가로길이는 1000이하
# 맨 왼쪽, 맨 오르쪽 두칸은 0으로 건물이 없다
# 각 빌딩의 높이의 최대는 255이다.

T = 10

for test_case in range(1,T+1):
    N = int(input())
    # 나중 출력할 때 {test_case}
    building_list = list(map(int, input().split()))
    # 4<= N <= 1000
    total_good_view = 0 # 조망권 가지는 세대 수
    hightest_building = 0
    #조망권은 최고층수 값 - 두번째 높은 층수
    for indx in range(2, N-2): #안에 있는 값들을 돌려서 최고 층수 찾아야함
        if building_list[indx] == 0:
            continue
        
        curr_building = building_list[indx]
        left_1_building = building_list[indx-1]
        left_2_building = building_list[indx-2]
        right_1_building = building_list[indx+1]
        right_2_building = building_list[indx+2]
        # 리스트를 for문으로 해보기!

        good_view = 0
        if curr_building > left_1_building and curr_building>left_2_building and curr_building > right_1_building and curr_building > right_2_building: #현재 반복된 값이 가장 높은 빌딩이라는 조건하에
            two_highest_building = 0 #두번째 빌딩을 임의로 설정
            if two_highest_building < left_1_building:
                two_highest_building = left_1_building
            if two_highest_building < left_2_building:
                two_highest_building = left_2_building
            if two_highest_building < right_1_building:
                two_highest_building = right_1_building
            if two_highest_building < right_2_building:
                two_highest_building = right_2_building

            good_view =  curr_building - two_highest_building
            total_good_view += good_view

    print(f'#{N} {total_good_view}')



  

    #코드 내에서 실현시켜야할 조건들
    '''
    왼쪽2개 빌딩 오른쪽2개 빌딩 보다 큰 값을 가져야 조망권 확보
    반복해서 얻은 값을 총_조망권에 할당
    제한 조건에 있는 건물이 없는 0의 경우도 포함 시켜야 한다.

    '''
