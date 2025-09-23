import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    omok_arr = [input() for _ in range(N)]
    result = 'NO'
    # 판정은 일단 NO로 임시확정

    #가로 5개 발견할  경우
    for i in range(N):
        for j in range(N):
            s = omok_arr[i][j]
            if s == 'o':  #o를 발견하게 될 경우 연속하는지 확인해야하니까
                # count += 1 #여기에다가 count를 두는 실수함!!
                for di, dj in [[1,0],[1,1],[0,1],[-1,1]]: #반복돌면서 지나온 부분에 대해서는 신경쓰지 않아도 되니까
                    count = 1 # 현재 o포함해서 1로 세팅해둔다.
                    for k in range(1,N): #최대 4개 더 체크하면 되는거니까 5까지 갈필요없음
                        #델타 탐색범위는 우, 우하 대각, 하, 좌하 대각만 하면된다.
                        ni = i + di*k
                        nj = j + dj*k
                        if 0<=ni<N and 0<=nj<N and omok_arr[ni][nj] == 'o':
                            count += 1
                        else:
                            break
                    if count == 5:
                        result = 'YES'




    print(f'#{tc} {result}')


