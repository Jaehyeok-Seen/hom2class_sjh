import sys
sys.stdin = open('input.txt')

T= int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [0] * (N* N +1) # 1번 ~ N^2 번 방번호

    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    # 현재 위치 숫자 기준 상하좌우를 확인
    # -> 1 큰게 있으면 visited에 1이라고 체크
    for y in range(N):
        for x in range(N):
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                #범위 밖 체크
                if ny < 0 or ny >= N or nx < 0 or nx >= N:
                    continue

                if arr[ny][nx] == arr[y][x] + 1:
                    #현재 숫자는 다음으로 이동 가능합니다!
                    visited[arr[y][x]] = 1
                    break # 다른 방향은 볼 필요 없다.
    # 연속된 1의 개수가 가장 긴 곳을 찾는다.
    max_cnt =0  # 정답
    cnt = 0  #하나하나 마다 몇개가 연속되는지?
    start = 0  #숫자를 세기 시작한 위치
    for i in range(1,N*N+1):
        if visited[i] ==1:
            cnt += 1
        else:
            if max_cnt < cnt:
                max_cnt = cnt  #최댓값 갱신
                start = i - cnt # 시작점 찾기
            cnt = 0 # 개수 초기화

    print(f'#{tc} {start} {max_cnt + 1}')