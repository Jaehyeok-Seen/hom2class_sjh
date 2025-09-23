# 10x10 배열에 빨강 파랑 칠하기
# N개 영역에 색을 칠해야하고, 왼쪽 상단 + 오른쪽 하단 모서리 인덱스 주어진다. => 범위 잘 지정하기
# 칠이 끝난 후 겹친 보라색이 된 칸 수를 구하는 프로그램 짜기
# 같은 색의 경우 겹치지 않는다.
# 행 r 열 c
# 예시 2 2 4 4 1 => [2,2]~[4,4]까지 color 1(빨강)으로 칠한다.
# 예시 3 3 6 6 2 => [3,3]~[6,6]까지 color 2(파랑)으로 칠한다.

#N개의 입력값을 받으면 그 중 앞 두개 + 뒤 두개 + 색깔 한개로 나누어서 받아야한다.

def painting(arr,r1,r2,c1,c2,color):

    for i in range(r1,r2+1):
        for j in range(c1,c2+1):
            if color == 1:
                arr[i][j] += 1
            elif color == 2:
                arr[i][j] += 2

    return arr


import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    canvas = [[0] * 10 for _ in range(11)]  # 10x10캔버스, [0]열개인 행, 0~9까지 반복


    for _ in range(N):
        r1,c1,r2,c2,color = list(map(int,input().split()))
        count = 0       #겹치는 부분 카운트한거
        painting(canvas,r1,r2,c1,c2,color)


        for i in range(10):  #그림그리는 함수에 의해 색칠완료된 canvas를 10개씩 다시 반복
            for j in range(10):
                if canvas[i][j] == 3 : # 그 값이 만약 3이라면 색깔이 겹치는 부분이니까 카운트1
                    count +=1

    print(f'#{tc} {count}')
