import sys
sys.stdin = open('algo1_sample_in.txt')


def cal(x, y):
    '''
    :param x: 시작 지점의 좌표 x
    :param y: 시작 지점의 좌표 y
    :return: 필터로 인한 연산 결과 누적값
    '''
    # print('시작지점', x, y)
    acc = 0
    # 모든 필터의 범위를 다 조사
    for i in range(M):
        for j in range(M):
            # 조사해야할 원본 데이터에서 얼마나 이동했느냐
            # 원래 시작지점 x, y에 대해, 이동한 거리 i, j를 각각 더해준다.
            target_x = x + i
            target_y = y + j
            acc += data[target_x][target_y] * filter[i][j]
    return acc


T = int(input())

for tc in range(1, T+1):
    # N: 입력층 크기, M: 필터 크기
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    filter = [list(map(int, input().split())) for _ in range(M)]
    output = [[0] * (N-M+1) for _ in range(N-M+1)]
    # print(output)
    # 내가 조사를 시작할 수 있는 좌표 x, y 범위 검증
    print(f'#{tc}')
    for x in range(N-M+1):
        for y in range(N-M+1):
            # x, y에서 시작한 결과 총 합이 얼마나오는지 보는 함수
            # print(cal(x, y), end=' ')
            output[x][y] = cal(x, y)
        # print()
    # print(output)
    for item in output:
        print(*item)
        # print(item[0], item[1], item[2], item[3])
    # tc
    # 출력층