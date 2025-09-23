import sys
sys.stdin = open('input.txt')

def calculate(row,arr,current_prob):
    global used, max_prob
    #가지치기가 필요
    if current_prob < max_prob:
        return

    if row == N:
        max_prob = max(max_prob, current_prob)
        return

    for col in range(N):
        if used[col]:
            continue

        used[col] = True #방문처리하고
        calculate(row+1,arr,current_prob*arr[row][col])
        used[col] = False



T=int(input())
for tc in range(1,T+1):
    N = int(input())
    work_percent = [list(map(int,input().split())) for _ in range(N)]
    # 행렬을 받아왔지만 정수형이 실제로는 퍼센트임
    transfer_work_percent = [[ing /100 for ing in work] for work in work_percent]

    used = [False] * N
    max_prob = 0


    calculate(0,transfer_work_percent,1.0)
    result = max_prob * 100
    # print(max_prob)
    print(f'#{tc} {result:.6f}')