import sys
sys.stdin = open('sample_input.txt')

T= int(input())
for tc in range(1,T+1):
    K, N, M = map(int,input().split())
    station = list(map(int,input().split()))
    current_position = 0
    cnt = 0


    while current_position + K < N:
        next_position = 0
        for charge in station:
            if current_position < charge <= current_position + K:
                next_position = charge

        current_position = next_position
        cnt +=1

        if not next_position:
            cnt = 0
            break

    print(f'#{tc} {cnt}')
