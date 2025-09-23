import sys
sys.stdin = open('5188_input.txt')

path = []

def moving(x,y,current_sum):
    global min_sum, arr

    if x == (N-1) and y == (N-1):
        min_sum = min(min_sum, current_sum)
        return

    #경계를 벗어나면 끝
    if x >= N or y >= N:
        return
    #오른쪽으로 이동할때의 재귀
    if x < N-1:
        moving(x+1, y, current_sum + arr[x+1][y])
    #아래쪽으로 이동할때의 재귀
    if y < N-1:
        moving(x,y+1, current_sum + arr[x][y+1])


T= int(input())
for tc in range(1,T+1):
    N = int(input()) #행렬의 크기
    arr = [list(map(int,input().split())) for _ in range(N)]
    #무조건 맨 왼쪽 위에서 => 오른쪽 아래까지 이동할 때,
    #지나는 칸에 써진 숫자의 합계가 최소가 되도록 움직인다면 이때의 합계를 출력
    min_sum = float('inf') #여기서 초기화 해줘야 반복되면서 각 케이스의 최소합이 나옴
    moving(0,0,arr[0][0])

    print(f'#{tc} {min_sum}')


    def judge(arr):
        my_cnt = False
        test = 0
        for num in arr:
            if test < num:
                test = num
                my_cnt = True
            else:
                my_cnt = False
                return

        return my_cnt


    T = int(input())
    for tc in range(1, T + 1):
        N, M = map(int, input().split())
        arr = list(map(int, input().split()))
        cnt = 0
        result = []

        for _ in range(M):
            window = arr[:M]
            result.append(window)
            for _ in range(M):
                if arr:
                    arr.pop(0)

        for i in range(len(result)):
            if judge(result[i]):
                cnt += 1

        print(f'#{tc} {cnt}')

