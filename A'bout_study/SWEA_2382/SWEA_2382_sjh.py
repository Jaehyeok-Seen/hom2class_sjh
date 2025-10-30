import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N,M,K = map(int,input().split())
    arr = [[0]*(N+2) for _ in range(N+2)]
    position = [[] for _ in range(K)]
    move_cnt = 0
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

    while move_cnt != M: #움직여야할 시간이 아직 안되었다면 움직여야함
        for x,y in position: # 미생물의 위치를 좌표로 꺼내서
            if arr[x][y][1] == 1: #상으로 움직임
                if 0< (x-1) < N+1: # 범위 안이라면
                    arr[x-1][y] = arr[x][y] #이동한 위치에 원래 값을 넣고
                    arr[x][y] = 0 #원래 위치에는 0으로 변경
                elif x-1 == 0 or x-1 == N+1: # 약품이 있는 곳에 도달한다면
                    arr[x-1][y] = (arr[x][y][0] // 2,2)
                    arr[x][y] = 0

            elif arr[x][y][1] == 2: #하로 움직임
                if 0< (x+1) < N+1: # 범위 안이라면
                    arr[x+1][y] = arr[x][y] #이동한 위치에 원래 값을 넣고
                    arr[x][y] = 0 #원래 위치에는 0으로 변경
                elif x-1 == 0 or x-1 == N+1: # 약품이 있는 곳에 도달한다면
                    arr[x+1][y] = (arr[x][y][0] // 2,1)
                    arr[x][y] = 0

            elif arr[x][y][1] == 3: #좌로 움직임
                if 0< (y-1) < N+1: # 범위 안이라면
                    arr[x][y-1] = arr[x][y] #이동한 위치에 원래 값을 넣고
                    arr[x][y] = 0 #원래 위치에는 0으로 변경
                elif y-1 == 0 or y-1 == N+1: # 약품이 있는 곳에 도달한다면
                    arr[x][y-1] = (arr[x][y][0] // 2,4)
                    arr[x][y] = 0

            else: #우로 움직임
                if 0< (y+1) < N+1: # 범위 안이라면
                    arr[x][y+1] = arr[x][y] #이동한 위치에 원래 값을 넣고
                    arr[x][y] = 0 #원래 위치에는 0으로 변경
                elif y+1 == 0 or y+1 == N+1: # 약품이 있는 곳에 도달한다면
                    arr[x][y+1] = (arr[x][y][0] // 2,3)
                    arr[x][y] = 0

        move_cnt +=1 #전부 다 움직이고 나면 단위시간 1 움직였다고 표시

    else:
        break
    print(f'#{tc} {remain}')

    """
    이동방향도 같이 저장해야함
    약품처리에 도달하게 되면 //2해주고 만약 군집의 수가 1이면 0으로 처리, 이동방향은 반대가 되어야함
    합쳐 진 군집의 미생물 수는 군집들의 미생물 수의 합이며, 이동 방향은 군집들 중 미생물 수가 가장 많은 군집의 이동방향이 된다. 
    합쳐지는 군집의 미생물 수가 같은 경우는 주어지지 않으므로 고려하지 않아도 된다.
    """
=================================================================================
import sys

sys.stdin = open('sample_input.txt')

T = int(input())`
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())

    # 미생물 정보를 리스트로 관리 [세로, 가로, 미생물수, 방향]
    microbes = []
    for i in range(K):
        sero, garo, num, dir = map(int, input().split())
        microbes.append([sero, garo, num, dir])

    # 방향별 이동 (1:상 2:하 3:좌 4:우)
    dx = [0, -1, 1, 0, 0]  # 인덱스 0은 사용안함
    dy = [0, 0, 0, -1, 1]

    # 방향 반대로 바꾸기
    opposite = [0, 2, 1, 4, 3]

    # M시간 동안 이동
    for _ in range(M):
        # 1. 모든 미생물 이동
        for microbe in microbes:
            x, y, num, dir = microbe
            nx = x + dx[dir]
            ny = y + dy[dir]

            # 2. 경계(약품)에 닿았는지 확인
            if nx == 0 or nx == N + 1 or ny == 0 or ny == N + 1:
                num = num // 2
                dir = opposite[dir]

            # 미생물 정보 업데이트
            microbe[0] = nx
            microbe[1] = ny
            microbe[2] = num
            microbe[3] = dir

        # 3. 미생물 수가 0인 것 제거
        microbes = [m for m in microbes if m[2] > 0]

        # 4. 같은 위치에 있는 군집 합치기
        position_dict = {}  # {(x,y): [[num, dir], [num, dir], ...]}

        for microbe in microbes:
            x, y, num, dir = microbe
            if (x, y) not in position_dict:
                position_dict[(x, y)] = []
            position_dict[(x, y)].append([num, dir])

        # 5. 합쳐진 결과로 새로운 microbes 리스트 만들기
        new_microbes = []
        for (x, y), groups in position_dict.items():
            if len(groups) == 1:  # 한 개만 있으면 그대로
                new_microbes.append([x, y, groups[0][0], groups[0][1]])
            else:  # 여러 개 있으면 합치기
                # 미생물 수가 가장 많은 군집 찾기
                max_num = max(groups, key=lambda g: g[0])[0]
                max_dir = [g[1] for g in groups if g[0] == max_num][0]

                # 모든 미생물 수 합치기
                total_num = sum(g[0] for g in groups)

                new_microbes.append([x, y, total_num, max_dir])

        microbes = new_microbes

    # 6. 남아있는 미생물 수 합계
    remain = sum(m[2] for m in microbes)

    print(f'#{tc} {remain}')
