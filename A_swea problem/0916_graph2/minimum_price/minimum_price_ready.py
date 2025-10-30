import sys
sys.stdin = open('sample_input.txt')

def find(sx,sy,fuel):
    global min_fuel

    if sx==N-1 and sy==N-1:
        #도착하면 종료
        min_fuel=min(fuel,min_fuel)
        return
    #가지치기 1
    if fuel >= min_fuel:
        return
    #가지치기 2
    if fuel >= min_fuel_to[sx][sy]:
        return
    min_fuel_to[sx][sy] = fuel


    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    for d in range(4):
        nx = sx + dx[d]
        ny = sy + dy[d]

        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            move_fuel = 1

            if arr[nx][ny] > arr[sx][sy]:
                diff = arr[nx][ny] - arr[sx][sy]
                move_fuel += diff

            visited[nx][ny] = True
            find(nx,ny,fuel + move_fuel)
            visited[nx][ny] = False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited=[[False]*N for _ in range(N)]
    visited[0][0] =True
    min_fuel_to = [[float('inf')]*N for _ in range(N)]
    min_fuel = float('inf')
    """
    이동시에 기본적으로 1씩 들고
    현재 위치값보다 큰 값으로 이동시 차이만큼 추가 연료 소비
    출발지는 0,0으로 고정, 도착지는 N-1,N-1
    """
    find(0,0,0)
    print(f'#{tc} {min_fuel}')

