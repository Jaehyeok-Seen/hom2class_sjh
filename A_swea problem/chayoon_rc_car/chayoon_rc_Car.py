import sys
sys.stdin = open('sample_input (1).txt')

def moving_rc( start_position, goal_position, curr_direction='U'):
    global field, command_list
    curr_position = start_position #시작 위치가 현재 위치

    for command in command_list:
        if command == 'L': # 왼쪽으로 90도 회전
            if curr_direction == 'U':
                curr_direction = 'L'
            elif curr_direction == 'R':
                curr_direction = 'U'
            elif curr_direction == 'D':
                curr_direction = 'R'
            elif curr_direction == 'L':
                curr_direction = 'D'

        elif command == 'R':  # 오른쪽으로 90도 회전
            if curr_direction == 'U':
                curr_direction = 'R'
            elif curr_direction == 'R':
                curr_direction = 'D'
            elif curr_direction == 'D':
                curr_direction = 'L'
            elif curr_direction == 'L':
                curr_direction = 'U'


        elif command == 'A':  # 앞으로 이동
            (r, c) = curr_position
            new_r, new_c = r, c  # 기본값은 현재 위치
            if curr_direction == 'U':  # 위로 이동
                new_r, new_c = r - 1, c
            elif curr_direction == 'D':  # 아래로 이동
                new_r, new_c = r + 1, c
            elif curr_direction == 'L':  # 왼쪽으로 이동
                new_r, new_c = r, c - 1
            elif curr_direction == 'R':  # 오른쪽으로 이동
                new_r, new_c = r, c + 1

            #경계 체크 및 장애물 체크
            if ( 0<= new_r < N and 0<= new_c < N and
                field[new_r][new_c] != 'T'):
                curr_position = (new_r,new_c)
            #else로 이동못하는 경우는 그대로 유지

    return 1 if curr_position == goal_position else 0

T=int(input())
for tc in range(1,T+1):
    N = int(input())
    field = [list(input()) for _ in range(N)]

    start_pos = None #(1, 1)
    end_pos = None #(3, 3)

    for row_idx, row in enumerate(field):
        for col_idx, value in enumerate(row):
            if value == 'X':
                start_pos = (row_idx, col_idx)
            elif value == 'Y':
                end_pos = (row_idx, col_idx)


    Q = int(input())
    results = []

    for _ in range(Q):
        line = input().split()
        C, command_list = int(line[0]), list(line[1]) # C는 커멘드의 길이를 의미
        #command별로 도달 할 수 있다면 1을 출력 아니라면 0을 출력
        #목적지에 이동 가능 여부가 아닌, 커맨드를 전부 실행 후 목적지에 도달했는지를 확인해야 함에 유의하라.
        result = moving_rc(start_pos,end_pos)
        results.append(str(result))

    print(f"#{tc} {' '.join(results)}")