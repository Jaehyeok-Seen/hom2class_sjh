
"""
1은 익은 토마토
0은 익지 않은 토마토
-1은 들어있지 않음

모두 익을 때까지 최소 몇일이 걸리는지 출력
[ 델타방향으로 0일 경우 1로 변경 ] + 범위체크


저장할때부터 모든 토마토가 익어있는 상태라면 0을 출력
토마토가 모두 익지 못하는 상황이면 -1

높이를 구현하는건 높이 2이상인겨우 같은자리의 값이
 
"""

def tomato(my_list,cnt):

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    for my_tuple in my_list:
        cur_i, cur_j = my_tuple
        for d in range(4):
            nx = cur_i + dx[d]
            ny = cur_j + dy[d]

            if 0<=nx< N and 0<=ny < M and arr[nx][ny] == 0:
                arr[nx][ny] = 1
                cnt += 1
            #불가능한 경우 더 추가해야할 것 같음
            elif 0<=nx< N and 0<=ny < M and arr[nx][ny] == -1:
                return -1

    return cnt

M,N,H = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
complete_tomato = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            complete_tomato.append((i,j))

result = tomato(complete_tomato,0)
print(result)