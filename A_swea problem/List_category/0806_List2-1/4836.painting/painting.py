def painting(arr,r1,r2,c1,c2,color):
    #N번을 칠하는데 색깔은 두종류 같은 색은 겹치지 않음
    for i in range(r1,r2+1):
        for j in range(c1,c2+1):
            if color == 1:
                arr[i][j] += 1
            elif color == 2:
                arr[i][j] += 2

    return arr


import sys
sys.stdin = open('sample_input.txt')
T = int(input()) #테스트케이스3

for tc in range(1,T+1):
    N = int(input()) #N번 영역을 칠할거다
    canvas = [[0]*10 for _ in range(11)] # 첨에 생각 못함

    # print(painting_list)
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        painting(canvas,r1,r2,c1,c2,color)

        count = 0

        for i in range(10):
            for j in range(10):
                if canvas[i][j] == 3:
                    count += 1

    print(f'#{tc} {count}')



# 10x10 배열에 빨강 파랑 칠하기
# N개 영역에 색을 칠해야하고, 왼쪽 상단 + 오른쪽 하단 모서리 인덱스 주어진다.
# 칠이 끝난 후 겹친 보라색이 된 칸 수를 구하는 프로그램 짜기
# 같은 색의 경우 겹치지 않는다.
# 행 r 열 c
# 예시 2 2 4 4 1 => [2,2]~[4,4]까지 color 1(빨강)으로 칠한다.
# 예시 3 3 6 6 2 => [3,3]~[6,6]까지 color 2(파랑)으로 칠한다.

#N개의 입력값을 받으면 그 중 앞 두개 + 뒤 두개 + 색깔 한개로 나누어서 받아야한다.