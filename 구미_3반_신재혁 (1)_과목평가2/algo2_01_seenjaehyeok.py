# 안전구역 수를 알아내기
# 가장가리 구역은 안전구역에서 제외 => 탐색범위를 줄여서 검색
# import sys
# sys.stdin = open('algo2_sample_in.txt')
#
T = int(input())

for tc in range(1,T+1):
    safe_count = 0 # 구해야할 안전지대 갯수(영향 x)

    N,M = map(int, input().split())

    map_arr = [list(map(int,input().split())) for _ in range(N)]  # 디지털 맵 불러오기

    for i in range(N):
        for j in range(M):   # 전체 맵 펼쳐서

             for l in range(1,N-1):
                 for m in range(1,M-1):
                     c = (l,m)
                     count = 0   #안전지대 개수 임시 카운트
        print(c)
        #     for dl,dm in [[-1,0],[1,0],[0,-1],[0,1]]: #상하좌우 탐색
        #         nl = l +dl
        #         nm = m +dm
        #         if 0<= nl < N and 0<= nm < M:
        #             if c > map_arr[nl][nm]:
        #                 count += 1
        # print(count)
        #
        #


