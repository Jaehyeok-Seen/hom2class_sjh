import sys
sys.stdin = open('sample_in.txt')

T=int(input())
for tc in range(1,T+1):
    #M번의 돌 뒤지깁, N개의 돌
    N,M = map(int,input().split())
    stone_list = list(input().split())
    # i번째 돌을 기준으로 마주보는 j개의 돌, 같은색이면 뒤집기

    for _ in range(M):
        i,j = map(int,input().split())

        for x in range(1,j+1):
            if (i-1)-x >= 0 and (i-1)+x < N:
                #(i-1) #인덱스를 기준으로 해야하니까
                L = (i-1) - x
                R = (i-1) + x

                if stone_list[L] == stone_list[R] :#같다면 뒤집는다
                    if stone_list[L]=='0': # 0일때는 1로
                        stone_list[L] = '1'
                        stone_list[R] = '1'
                    else: #1일때는 0으로
                        stone_list[L] = '0'
                        stone_list[R] = '0'
                else: #다르다면 패스
                    pass

    print(f'#{tc}', ' '.join(stone_list))






    # print(f'#{tc} {}')