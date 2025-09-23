import sys
sys.stdin = open('sample_input.txt')

# 제한 사항 가로길이는 1000이하
# 맨 왼쪽, 맨 오르쪽 두칸은 0으로 건물이 없다
# 각 빌딩의 높이의 최대는 255이다.

T = 10

for tc in range(1,T+1):
    N = int(input())        #N = 건물의 개수
    building_list = list(map(int, input().split()))
    # print(building_list)

    # 조망권 확보 = 왼쪽 2칸 오른쪽 2칸보다 높은 건물만이 가진다
    # left1,left2,right1,right2 각 변수에 기준건물 주변 높이 비교
    # 그랬을 때 가장 높은 건물일 경우 2번째 높은 건물과의 차이가 조망권세대 수
    # 건물 리스트 중에 조망권 세대 수의 합이 = result

    zomang_sum = 0
    
    
    for i in range(2,N-2):
        max_height = building_list[0]
        left1 = building_list[i-1]
        left2 = building_list[i-2]
        right1 = building_list[i+1]
        right2 = building_list[i+2]
        

        if max_height < building_list[i]:
            max_height = building_list[i]

            if max_height > left1 and max_height > left2 and max_height >right1 and max_height>right2:
                list1 = [max_height -left1, max_height - left2, max_height - right1,max_height - right2]
                zomang = min(list1)
                zomang_sum += zomang
    
    print(f'#{tc} {zomang_sum}')

