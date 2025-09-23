# N개의 줄이 주어진다.
# NxN 크기의 우주 영역 정보
# 우주의 빈공간은 '0', 별은 '*'

# 파리퇴치랑 비슷하게 델타로 MxM 영역만 탐색 가능한 상황
# 결과 : 정확히 K개의 별을 포함하는 M*M영역을 찾는 것(조건을 만족하는 영역은 1개 이하다)
import sys
sys.stdin = open('algo1_sample_in.txt')

T = int(input())

for tc in range(1,T+1):
    N,M,K = map(int,input().split()) # N : 우주크기 M : 스카우터 확인범위 K : 찾아야 할 별의 갯수

    space_list = [list(map(str,input())) for _ in range(N)] # 리스트 생성 확인 완료

    star_result = f"{-1} {-1}"   #상단 좌측 모서리의 좌표를 출력시키는 게 문제

    for i in range(N-M+1):
        for j in range(N-M+1):   # 우주를 다 풀어두는 작업 완료

            center = space_list[i][j]   # 스카우터 영역의 기준점
            count = 0
            for di in range(M): # 좌측상단 모서리 좌표를 기준으로 스카우터 범위를 미리 설정
                for dj in range(M):
                    ni = i+di
                    nj = j+dj
                   
                    if 0<= ni < N and 0<= nj < N: #스카우터가 바깥으로 넘어가지 않게 제한설정
                        if space_list[ni][nj] == '*':
                            count += 1
                    
            if count == K:
                star_result = f"{i} {j}"
                break
         
                     
    print(star_result)
    # print(f'#{tc} {star_result}')



# 제출버전
# for tc in range(1,T+1):
#     N,M,K = map(int,input().split()) # N : 우주크기 M : 스카우터 확인범위 K : 찾아야 할 별의 갯수

#     space_list = [list(map(str,input())) for _ in range(N)] # 리스트 생성 확인 완료

#     star_result = 0   #상단 좌측 모서리의 좌표를 출력시키는 게 문제

#     for i in range(N):
#         for j in range(N):   # 우주를 다 풀어두는 작업 완료

#             center = space_list[i][j]   # 스카우터 영역의 기준점
#             explore_list = []
#             for di in range(N-M+1): # 좌측상단 모서리 좌표를 기준으로 스카우터 범위를 미리 설정
#                 for dj in range(N-M+1):
#                     ni = i+di
#                     nj = j+dj
#                     # print(f'ni={ni},nj={nj}')
                   
#                     if 0<= ni < N and 0<= nj < M: #스카우터가 바깥으로 넘어가지 않게 제한설정
#                         explore_list.append(space_list[ni][nj])

#                 if explore_list.count('*') == K:
#                     star_result = [i,j]
#                 else:
#                     star_result = '-1 -1'
#     print(explore_list)
#     # print(f'#{tc} {star_result}')













