import sys
import socket
from collections import deque

##############################
# 메인 프로그램 통신 변수 정의
##############################
# 게임 서버와의 통신을 위한 네트워크 설정
HOST = '127.0.0.1'  # 로컬호스트 (같은 컴퓨터)
PORT = 8747  # 통신에 사용할 포트 번호
ARGS = sys.argv[1] if len(sys.argv) > 1 else ''  # 명령행 인수 받기
sock = socket.socket()  # TCP 소켓 생성


##############################
# 메인 프로그램 통신 함수 정의
##############################

def init(nickname):
    """게임 서버에 최초 연결하고 닉네임을 등록하는 함수"""
    try:
        print(f'[STATUS] Trying to connect to {HOST}:{PORT}...')
        sock.connect((HOST, PORT))  # 서버에 연결
        print('[STATUS] Connected')
        init_command = f'INIT {nickname}'  # 초기화 명령어 생성
        return submit(init_command)  # 서버에 전송하고 응답 받기
    except Exception as e:
        print('[ERROR] Failed to connect. Please check if the main program is waiting for connection.')
        print(e)


def submit(string_to_send):
    """서버에 명령어를 전송하고 응답을 받는 함수"""
    try:
        send_data = ARGS + string_to_send + ' '  # 전송할 데이터 준비
        sock.send(send_data.encode('utf-8'))  # UTF-8로 인코딩해서 전송
        return receive()  # 서버 응답 받기
    except Exception as e:
        print('[ERROR] Failed to send data. Please check if connection to the main program is valid.')
    return None


def receive():
    """서버로부터 게임 데이터를 받는 함수"""
    try:
        game_data = (sock.recv(1024)).decode()  # 1024바이트까지 받아서 디코딩
        # 첫 글자가 숫자이고 0보다 크면 유효한 데이터
        if game_data and game_data[0].isdigit() and int(game_data[0]) > 0:
            return game_data
        print('[STATUS] No receive data from the main program.')
        close()  # 유효하지 않으면 연결 종료
    except Exception as e:
        print('[ERROR] Failed to receive data. Please check if connection to the main program is valid.')


def close():
    """네트워크 연결을 종료하는 함수"""
    try:
        if sock is not None:
            sock.close()
        print('[STATUS] Connection closed')
    except Exception as e:
        print('[ERROR] Network connection has been corrupted.')


##############################
# 입력 데이터 변수 정의
##############################
# 게임에서 받아온 데이터를 저장할 전역 변수들
map_data = [[]]  # 게임 맵 정보 (2차원 배열)
my_allies = {}  # 아군 정보 (딕셔너리: 이름->정보)
enemies = {}  # 적군 정보 (딕셔너리: 이름->정보)
codes = []  # 암호문 정보 (리스트)


##############################
# 입력 데이터 파싱
##############################

def parse_data(game_data):
    """서버에서 받은 게임 데이터를 파싱해서 각 변수에 저장하는 함수"""
    game_data_rows = game_data.split('\n')  # 줄바꿈으로 분리
    row_index = 0  # 현재 처리 중인 행 인덱스

    # 1. 헤더 정보 파싱 (첫 번째 줄)
    header = game_data_rows[row_index].split(' ')
    map_height = int(header[0]) if len(header) >= 1 else 0  # 맵 높이
    map_width = int(header[1]) if len(header) >= 2 else 0  # 맵 너비
    num_of_allies = int(header[2]) if len(header) >= 3 else 0  # 아군 수
    num_of_enemies = int(header[3]) if len(header) >= 4 else 0  # 적군 수
    num_of_codes = int(header[4]) if len(header) >= 5 else 0  # 암호문 수
    row_index += 1  # 다음 줄로 이동

    # 2. 맵 데이터 파싱 (map_height 줄만큼)
    map_data.clear()  # 기존 데이터 초기화
    map_data.extend([['' for c in range(map_width)] for r in range(map_height)])
    for i in range(0, map_height):
        col = game_data_rows[row_index + i].split(' ')  # 각 행을 공백으로 분리
        for j in range(0, len(col)):
            map_data[i][j] = col[j]  # 각 셀에 값 저장
    row_index += map_height  # 맵 데이터만큼 행 인덱스 증가

    # 3. 아군 정보 파싱 (num_of_allies 줄만큼)
    my_allies.clear()  # 기존 데이터 초기화
    for i in range(row_index, row_index + num_of_allies):
        ally = game_data_rows[i].split(' ')  # 공백으로 분리
        ally_name = ally.pop(0) if len(ally) >= 1 else '-'  # 첫 번째는 이름
        my_allies[ally_name] = ally  # 나머지는 정보 (체력, 방향 등)
    row_index += num_of_allies

    # 4. 적군 정보 파싱 (num_of_enemies 줄만큼)
    enemies.clear()  # 기존 데이터 초기화
    for i in range(row_index, row_index + num_of_enemies):
        enemy = game_data_rows[i].split(' ')  # 공백으로 분리
        enemy_name = enemy.pop(0) if len(enemy) >= 1 else '-'  # 첫 번째는 이름
        enemies[enemy_name] = enemy  # 나머지는 정보
    row_index += num_of_enemies

    # 5. 암호문 정보 파싱 (num_of_codes 줄만큼)
    codes.clear()  # 기존 데이터 초기화
    for i in range(row_index, row_index + num_of_codes):
        codes.append(game_data_rows[i])  # 암호문 그대로 저장


def print_data():
    """파싱된 게임 데이터를 보기 좋게 출력하는 함수"""
    print(f'\n----------입력 데이터----------\n{game_data}\n----------------------------')

    # 맵 정보 출력
    print(f'\n[맵 정보] ({len(map_data)} x {len(map_data[0])})')
    for i in range(len(map_data)):
        for j in range(len(map_data[i])):
            print(f'{map_data[i][j]} ', end='')  # 각 셀 출력
        print()  # 줄바꿈

    # 아군 정보 출력
    print(f'\n[아군 정보] (아군 수: {len(my_allies)})')
    for k, v in my_allies.items():
        if k == 'M':  # 내 탱크
            print(f'M (내 탱크) - 체력: {v[0]}, 방향: {v[1]}, 보유한 일반 포탄: {v[2]}개, 보유한 메가 포탄: {v[3]}개')
        elif k == 'H':  # 아군 포탑
            print(f'H (아군 포탑) - 체력: {v[0]}')
        else:  # 다른 아군 탱크
            print(f'{k} (아군 탱크) - 체력: {v[0]}')

    # 적군 정보 출력
    print(f'\n[적군 정보] (적군 수: {len(enemies)})')
    for k, v in enemies.items():
        if k == 'X':  # 적군 포탑
            print(f'X (적군 포탑) - 체력: {v[0]}')
        else:  # 적군 탱크
            print(f'{k} (적군 탱크) - 체력: {v[0]}')

    # 암호문 정보 출력
    print(f'\n[암호문 정보] (암호문 수: {len(codes)})')
    for i in range(len(codes)):
        print(codes[i])


##############################
# 닉네임 설정 및 최초 연결
##############################
NICKNAME = '기본코드'
game_data = init(NICKNAME)  # 서버에 연결하고 첫 게임 데이터 받기


###################################
# 알고리즘 함수/메서드 부분 구현
###################################

def find_positions(grid, start_mark, goal_mark):
    """맵에서 시작점과 목표점의 좌표를 찾는 함수"""
    rows, cols = len(grid), len(grid[0])
    start = goal = None

    # 맵 전체를 순회하면서 특정 마크를 찾기
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == start_mark:  # 시작점 발견
                start = (row, col)
            elif grid[row][col] == goal_mark:  # 목표점 발견
                goal = (row, col)
    return start, goal


def in_range_and_clear(grid, pos, target, wall, max_range=3):
    """목표가 사거리 내 직선상에 있고 시야가 차단되지 않는지 확인하는 함수"""
    r, c = pos  # 현재 위치
    tr, tc = target  # 목표 위치

    # 같은 행에 있는 경우 (좌우 방향)
    if r == tr:
        step = 1 if tc > c else -1  # 오른쪽이면 1, 왼쪽이면 -1
        for d in range(1, max_range + 1):  # 사거리만큼 확인
            nc = c + step * d  # 다음 확인할 열 위치
            if not (0 <= nc < len(grid[0])):  # 맵 범위 벗어나면 중단
                break
            if grid[r][nc] == wall:  # 바위(벽)가 있으면 시야 차단
                break
            if (r, nc) == target:  # 목표를 찾았으면
                return True, 0 if step == 1 else 2  # (발견여부, 방향)

    # 같은 열에 있는 경우 (상하 방향)
    if c == tc:
        step = 1 if tr > r else -1  # 아래쪽이면 1, 위쪽이면 -1
        for d in range(1, max_range + 1):  # 사거리만큼 확인
            nr = r + step * d  # 다음 확인할 행 위치
            if not (0 <= nr < len(grid)):  # 맵 범위 벗어나면 중단
                break
            if grid[nr][c] == wall:  # 바위(벽)가 있으면 시야 차단
                break
            if (nr, c) == target:  # 목표를 찾았으면
                return True, 1 if step == 1 else 3  # (발견여부, 방향)

    return False, None  # 사거리 내 직선상에 없음


def bfs(grid, start, target, blocked, wall):
    """BFS 알고리즘으로 최단 경로를 찾는 함수"""
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start, [])])  # (현재위치, 지금까지의 행동목록)
    visited = {start}  # 방문한 위치들

    while queue:
        (r, c), actions = queue.popleft()  # 큐에서 하나 꺼내기

        # 현재 위치에서 목표를 공격할 수 있는지 확인
        in_range, direction = in_range_and_clear(grid, (r, c), target, wall, 3)
        if in_range:  # 공격 가능하면
            return actions + [FIRE_CMDS[direction]]  # 지금까지 행동 + 공격 명령

        # 4방향으로 이동 시도
        for d, (dr, dc) in enumerate(DIRS):
            nr, nc = r + dr, c + dc  # 다음 위치 계산
            # 맵 범위 내이고, 이동 가능하고, 아직 방문하지 않았다면
            if (0 <= nr < rows and 0 <= nc < cols and
                    grid[nr][nc] not in (wall, 'W') and (nr, nc) not in visited):
                visited.add((nr, nc))  # 방문 체크
                # 큐에 추가 (다음위치, 지금까지행동+이동명령)
                queue.append(((nr, nc), actions + [MOVE_CMDS[d]]))

    return []  # 경로를 찾을 수 없음


# 게임에서 사용할 상수들 정의
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우, 하, 좌, 상 방향벡터
MOVE_CMDS = {0: "R A", 1: "D A", 2: "L A", 3: "U A"}  # 각 방향별 이동 명령
FIRE_CMDS = {0: "R F", 1: "D F", 2: "L F", 3: "U F"}  # 각 방향별 공격 명령
START_SYMBOL = 'M'  # 내 탱크 표시
TARGET_SYMBOL = 'X'  # 적군 포탑 표시
BLOCKED = {'R', 'W'}  # 이동할 수 없는 지형 (바위, 물)
WALL_SYMBOL = 'R'  # 시야를 차단하는 벽 (바위)

# 첫 게임 데이터로 초기 경로 계산
parse_data(game_data)  # 받은 데이터 파싱
start, target = find_positions(map_data, START_SYMBOL, TARGET_SYMBOL)  # 시작점, 목표점 찾기

if not start or not target:  # 시작점이나 목표점을 찾을 수 없으면
    print("[ERROR] Start or target not found in map")
    close()
    exit()

# BFS로 최적 경로 계산
actions = bfs(map_data, start, target, BLOCKED, WALL_SYMBOL)

# 메인 게임 루프
while game_data is not None:  # 게임 데이터가 있는 동안 계속
    print_data()  # 현재 게임 상태 출력

    # 실행할 행동이 없으면 새로 계산
    if not actions:
        start, target = find_positions(map_data, START_SYMBOL, TARGET_SYMBOL)
        actions = bfs(map_data, start, target, BLOCKED, WALL_SYMBOL) if start and target else []

    # 다음 행동 결정
    output = actions.pop(0) if actions else 'A'  # 계획된 행동이 있으면 실행, 없으면 전진

    # 서버에 명령 전송하고 다음 게임 데이터 받기
    game_data = submit(output)
    if game_data:
        parse_data(game_data)  # 새 데이터 파싱

close()  # 게임 종료 시 연결 닫기