import sys
sys.stdin = open('sample_in.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())

    space_arr = [list(map(int,input().split())) for _ in range(N)]


    monster = None


    for i in range(N):
        for j in range(N):
            if space_arr[i][j] == 2:
                monster = (i,j)

            for di, dj in [[-1,0],[1,0],[0,-1],[0,1]]:
                k = 1
                while True:
                    ni = i + di*k
                    nj = j + dj*k

                    if 0<= ni <N and 0 <= nj < N:
                        if space_arr[ni][nj] == 0:
                            space_arr[ni][nj] = 3
                            k += 1
                        elif space_arr[ni][nj] ==1:
                            break
                        else:
                            k += 1
                    else:#경계 벗어난다면
                        break



