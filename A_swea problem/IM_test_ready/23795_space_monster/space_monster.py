import sys
sys.stdin = open('sample_in.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())

    space_arr = [list(map(int,input().split())) for _ in range(N)]

    # 괴물의 경우 2인 위치가 괴물의 위치
    # 벽은 1
    # 안전공간 즉 빈칸은 0이다.
    # 괴물 위치 2에서 상하좌우 델타탐색으로 0인 공간을 만나면 다 3으로 바꾼다. 1을 만나면 스톱
    # 마지막에 0인 곳이 몇개인지 세면 된다.
    monster = None


    for i in range(N):
        for j in range(N):
            if space_arr[i][j] == 2:
                monster = (i,j)


                for di, dj in [[-1,0],[1,0],[0,-1],[0,1]]: #상하좌우순
                    for k in range(1,N+1):  #범위때문에 6개만 맞는 오답이 나옴, 오목의 경우 4개만 더 보면 됐던거라 다름
                        ni = i + di*k
                        nj = j + dj*k
                        if 0<=ni<N and 0<=nj<N and space_arr[ni][nj] == 0:
                            space_arr[ni][nj] = 3
                        elif 0<=ni<N and 0<=nj<N and space_arr[ni][nj] == 1:
                            break
    zero_count = 0
    for k in range(N):
        for l in range(N):
            if space_arr[k][l] == 0:
                zero_count += 1

    print(f'#{tc} {zero_count}')



