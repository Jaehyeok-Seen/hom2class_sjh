import sys
sys.stdin = open('sample_input.txt')

#1. 종료조건 : 숫자 7자리일 때 종료
#2. 가지의 수  : 4개 (상하좌우)
def recur(y,x, number):
    if len(number) == 7: #7자리면 종료
        result.add(number) #set에 추가
        return
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    for i in range(4): #상하좌우
        ny = y + dy[i]
        nx = x + dx[i]

        #범위밖 체크는 무조건, 범위 밖이면 다음 방향 확인(continue)
        if ny < 0 or ny >=4 or nx < 0 or nx>=4:
            continue
        recur(ny, nx, number+matrix[ny][nx])



T= int(input())
for tc in range(1,T+1):
    matrix = [input().split() for _ in range(4)]
    result = set()

    #7자리 만드는 코드
    # -4 * 4 가 모두 출발점이 될 수 있다.
    for start_y in range(4):
        for start_x in range(4):
            recur(start_y,start_x, matrix[start_y][start_x])

    #숫자라고 숫자로만 받지말고, 문제해결에 문자가 더편한지 판단 필요
    print(f'#{tc} {len(result)}')