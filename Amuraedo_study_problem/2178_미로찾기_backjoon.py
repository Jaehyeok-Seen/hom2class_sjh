# def moving(cur_x, cur_y, curr_cnt):
#     global min_cnt
#     if cur_x == N - 1 and cur_y == M - 1:
#         # 좌표가 지정된 N,M에ㅔ 도착하면 종료
#         min_cnt = min(min_cnt, curr_cnt)
#         return
#
#     dx = [-1,1,0,0]
#     dy = [0,0,-1,1]
#
#     for d in range(4):
#         nx = cur_x + dx[d]
#         ny = cur_y + dy[d]
#
#         if 0 <= nx < N and 0 <= ny < M:
#             if arr[nx][ny] == 1:
#                 cur_x, cur_y = nx, ny
#                 curr_cnt += 1
#             else:
#                 continue
#
#
# N,M = map(int,input().split())
# arr = [list(map(int,input())) for _ in range(N)]
# min_cnt = 10000
# moving(0,0,1)
# print(min_cnt)
# """
# 미로에서 1은 이동, 0은 이동불가능
# 1,1에서 출발해서 N,M의 위치로 이동할 때 지나야하는 최소의 칸 수를 구하는 프로그램
# 인덱스 이용시
# (0,0)에서 (N-1,M-1)로 이동
# 서로 인접한 칸으로만 이동가능
# 델타 탐색
# """
# ==================================================================================

def moving(cur_x, cur_y, curr_cnt):
    global min_cnt
    if cur_x == N - 1 and cur_y == M - 1:
        # 좌표가 지정된 N,M에ㅔ 도착하면 종료
        min_cnt = min(min_cnt, curr_cnt)
        return

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    for d in range(4):
        nx = cur_x + dx[d]
        ny = cur_y + dy[d]

        if 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                moving(nx,ny,curr_cnt+1)
                visited[nx][ny] = False


N,M = map(int,input().split())
arr = [list(map(int,input())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
# print(visited)
min_cnt = 10000
moving(0,0,1)
print(min_cnt)
"""
미로에서 1은 이동, 0은 이동불가능
1,1에서 출발해서 N,M의 위치로 이동할 때 지나야하는 최소의 칸 수를 구하는 프로그램
인덱스 이용시
(0,0)에서 (N-1,M-1)로 이동
서로 인접한 칸으로만 이동가능
델타 탐색
"""
