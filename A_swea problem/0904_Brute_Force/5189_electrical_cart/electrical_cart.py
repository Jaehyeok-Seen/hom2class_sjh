"""
골프장 관리를 위해 전기 카트로
사무실 -> 관리구역 -> 사무실
사무실에서 출발해 각 구역을 한 번씩만 방문하고 사무실로 돌아올 때의 최소 배터리를 구하시오
1번은 사무실 2번~N번은 관리구역 번호
경로의 앞 뒤 시작이 정해진 채로 안쪽 경로를 순열로 찾아야한다.
그 중 순열에 해당하는 값들을 저장해서 비교한 후 최소가 되는 경우 출력
1부터 N까지 순열을 전부 구한다.
1은 고정이니까 인덱스 2번부터 N까지


"""

def moving_cart(num):
    global path, used, N, min_electric

    used[1]=True
    cost = 0
    if num == N:
        complete_path = path + [1]

        for i in range(N):
            cost += mapping[complete_path[i]-1][complete_path[i + 1]-1]
        min_electric = min(min_electric,cost)

        return

    for indx in range(2,N+1):
        if used[indx]:
            continue
        used[indx] = True
        path.append(indx)
        moving_cart(num+1)
        path.pop()
        used[indx] = False
    # path.append(1)




import sys
sys.stdin = open('5189_input.txt')

T = int(input())
for tc in range(1,T+1):
    path = [1]
    N= int(input()) #행렬의 크기
    used = [False] * (N+1)
    min_electric = float('inf')
    mapping = [list(map(int,input().split())) for _ in range(N)]
    moving_cart(1)
    print(f'#{tc} {min_electric})
    # 복사된 경로를 통해 mapping의 값을 실제로 대입해서 최소값찾아야함


