def DFS(s ):
    global used, N, path, min_sum
    current_sum = 0

    if s == N : #종료 조건 경로 탐색 중 N이 마지막이니까
        #뭘할지는 비워둠
        #마지막 경로에 1을 더해줘야 우리가 원하는 목표
        final_path = path + [1]
        for i in range(N):
            current_sum += arr[final_path[i]-1][final_path[i+1]-1]
        min_sum = min(min_sum,current_sum)
        return

    for i in range(2, N+1): #시작점은 무조건 [1] 고정이기때문
        if used[i]:
            continue
        used[i] = True
        path.append(i)
        DFS(s+1)
        used[i] = False
        path.pop()


import sys
sys.stdin = open('5189_input.txt')
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    path = [1]
    used = [False] * (N+1) # 0까지 만들어서 인덱스 맞출거니까
    min_sum = float('inf')  #문제에서 요구하는 최소전기사용량을 무한대로 설정
    #함수 안에 넣으면 계속 바뀌게됨 지금 위치가 맞음
    used[1] = True #시작점은 방문한걸로 치기

    DFS(1)


    print(f'#{tc} {min_sum}')