import sys
sys.stdin = open('5189_input.txt')
T=int(input())

def DFS(s):
    global used,N,path,min_sum

    if s ==N:
        final_path = path +[1]
        for i in range(N):
            current_sum = sum(arr[a-1][b-1] for a,b in zip(final_path,final_path[1:]))
        min_sum = min(min_sum, current_sum)
        return

    for i in range(2,N+1):
        if used[i]:
            continue
        used[i] = True
        path.append(i)
        DFS(s+1)
        path.pop()
        used[i] = False




for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    used = [False] *(N+1)
    path = [1]
    min_sum = float('inf')
    used[1] = True

    DFS(1)

    print(f'#{tc} {min_sum}')