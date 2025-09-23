import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    count = 0
    for x in range(-N,N+1):
        for y in range(-N,N+1):
            if (x**2) + (y**2) <= N**2:
                count += 1
    # 처음에 range좌표를 잘못해서 1사분면만 해당하는 값만 나왔음..

    print(f'#{tc} {count}')
