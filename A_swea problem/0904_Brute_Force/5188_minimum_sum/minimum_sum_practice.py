import sys
sys.stdin = open('5188_input.txt')

def dfs(curr_x,curr_y,curr_sum):
    global min_sum
    if curr_x == N-1 and curr_y == N-1:
        min_sum = min(min_sum, curr_sum)
        return

    if curr_x > N-1 or curr_y > N-1 :
        #범위를 넘어가면 종료
        return
    if curr_x < N-1:
        dfs(curr_x + 1, curr_y, curr_sum + arr[curr_x+1][curr_y])
    if curr_y < N-1:
        dfs(curr_x, curr_y+1, curr_sum+arr[curr_x][curr_y+1])



T= int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split()))for _ in range(N)]
    min_sum = float('inf')
    dfs(0,0,arr[0][0])
    print(min_sum)

# print(f'#{tc} {result}')
