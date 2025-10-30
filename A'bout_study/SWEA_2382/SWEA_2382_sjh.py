import sys
sys.stdin = open('sample_input.txt')

# def moving(time_cnt): #단위시간별 움직이는 걸 함수로 정의, 즉 M시간만큼 움직임을 반복
#     for time in range(1,time_cnt+1):
#
#  # arr = -1 일경우 약품에 들어간거로 간주
#     if arr[i][j] == -1:
#         num = num // 2

T = int(input())
for tc in range(1, T+1):
    N,M,K = map(int,input().split())
    arr = [[0]*(N+2) for _ in range(N+2)]
    position = [[] for _ in range(K)]
    for i in range(K):
        sero, garo, num, dir = map(int,input().split())
        arr[sero][garo] = (num,dir) #1:상 2:하 3:좌 4:우
        position[i].append((sero,garo))
    #패딩 처리 -1로
    for i in range(N+2):
        arr[0][i] = -1
        arr[N+1][i] = -1
    for i in range(N+2):
        arr[i][0] = -1
        arr[i][N+1] = -1

    #위에까지 재료준비 완료
    print(position)

    remain = 0 #M시간 후 남아있는 미생물 수의 총 합

    for time in range(1,M+1):
        if dir == 1:
            pass
        elif dir == 2:
            pass
        elif dir == 3:
            pass
        else:
            pass

    print(f'#{tc} {remain}')

    """
    이동방향도 같이 저장해야함
    약품처리에 도달하게 되면 //2해주고 만약 군집의 수가 1이면 0으로 처리, 이동방향은 반대가 되어야함
    합쳐 진 군집의 미생물 수는 군집들의 미생물 수의 합이며, 이동 방향은 군집들 중 미생물 수가 가장 많은 군집의 이동방향이 된다. 
    합쳐지는 군집의 미생물 수가 같은 경우는 주어지지 않으므로 고려하지 않아도 된다.
    """

