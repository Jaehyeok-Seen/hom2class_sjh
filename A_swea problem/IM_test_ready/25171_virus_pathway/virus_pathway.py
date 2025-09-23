import sys
sys.stdin = open('sample_input.txt')


def virus_move():
    # 바이러스는 상하 좌우 네방향으로만 이동
    global start_x, start_y, infection_area, city_arr, N

    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while True:
        next = None
        min_point = city_arr[start_x][start_y]  # 임의로 시작점을 기준으로 잡아둠, 시작점보다 작아야 전파가능
        for di, dj in direction:
            ni = start_x + di
            nj = start_y + dj

            # 인접한 구역 중 현재보다 가장 낮은 면역력을 가진 곳으로만 전염
            # 다음 지점을 탐색하기 위한 for문
            if 0 <= ni < N and 0 <= nj < N: #제한된 크기 안에 있어야하고
                if city_arr[ni][nj] < city_arr[start_x][start_y] and city_arr[ni][nj] < min_point:
                    #시작점보다 작으면서, 그 중 최소인 지점이어야 다음 지점이 된다.
                    min_point = city_arr[ni][nj]
                    next = (ni, nj)

        if next is None: # 다음 지점이 존재하지 않을때 벗어나는 조건 걸어두기
            break

        start_x, start_y = next
        infection_area += 1


T = int(input()) # 3
for tc in range(1,T+1):
    N = int(input())  #N x N
    city_arr = [list(map(int,input().split())) for _ in range(N)]

    start_x, start_y = (0, 0)
    max_point = 0
    infection_area = 0 # 구해야할 값

    for i in range(N):
        for j in range(N):
            #virus start , max_city_arr인 지점에서
            # 도시에서 가장 면역력이 높은 구역에서 최초로 발생
            if city_arr[i][j] > max_point:
                max_point = city_arr[i][j]
                start_x = i
                start_y = j

    infection_area = 1
    virus_move()


    #==========================================


    print(f'#{tc} {infection_area}')




# 전염 가능한 곳은 0개 또는 1개임이 보장
# 바이러스는 더 이상 전염할 수 없을 때까지 확산
# 이때 전염된 구역의 최대 개수를 출력
