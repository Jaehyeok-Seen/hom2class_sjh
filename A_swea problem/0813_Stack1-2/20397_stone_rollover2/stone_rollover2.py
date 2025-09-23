# 동전처럼 생긴 돌의 양면은 각각 흰색 , 검은색
# i번째 돌을 두고 (기준) 마주보는j개의 돌에 대해, 같은 색이면 뒤집고 다른색이면 둔다
# 주어진 돌을 벗어나는 경우 뒤집기는 중단(break)


# 함수정의해서 실시할 생각

def rollover(list,N,i,j): # 한 리스트에 대해 크기를 받아서 뒤집기하는 함수
    #i돌을 기준으로 마주보는 j개의 돌 rollover 실시 (i는 인덱싱이 아닌 1부터)
    #list[i-1]에서 list[i-2]와 list[i] 같다면 1,0을 바꾸고 다르다면 그대로 둔다.
    # 뒤집기 횟수만큼 반복해야함
    # for test in range(M):
    base = i - 1 #주어지는 i는 인덱스값이 아니라서 -1해준다.

    for indx in range(1,j+1): # 마주보는 j개의 돌을 뒤집어야하기 때문에 반복 ㄱㄱ
        left = base - indx
        right = base + indx

        if 0 <= i-1-indx and i-1+indx < N : #벗어난다면 그즉시 종료
            if list[left] == list[right]:
                if list[left] == 0:
                    list[left] = 1
                    list[right] = 1
                elif list[right] == 1:
                    list[left] = 0
                    list[right] = 0
                else:
                    list[right] = 0
            else:
                pass
        else:
            break

    return list


import sys
sys.stdin = open('sample_in.txt')

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    stone_list = list(map(int,input().split())) 
    ij_list = [tuple(map(int,input().split())) for _ in range(M)]
    # [(3, 2), (5, 3), (4, 4), (8, 4)] = ij_list
    for i, j in ij_list: #각각 풀어서 i,j에 할당하기 위한 코드
       rollover(stone_list, N,i,j)

    print(f'#{tc}', *stone_list)