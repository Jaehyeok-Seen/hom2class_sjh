import sys
sys.stdin = open('sample_input (3).txt')

"""
A사에서 새로 생산되는 N종의 제품을 N곳의 공장에서 
한곳당 하나씩
각 제품별 생산비용이 주어질 때 최소 생산 비용을 계산
행은 제품, 열은 공장 한곳당 하나씩이니까
visited해서 방문처리후 중복 없이 한개씩 선택 할 수 있도록
"""
def recur(indx,cur_price):
    global min_price
    if indx == N:
        #제품 인덱스가 끝나면 종료
        #그때 해야할 일은 최소값
        min_price = min(min_price , cur_price)
        return
    #더이상 비교할 필요없는 경우는 종료조건에 걸리기 전 최소비용보다 크다면 의미가 없다.
    if cur_price >= min_price:
        return
    # 남은 제품들(indx+1부터 N-1까지)의 최소 비용 계산
    remaining_min = 0

    for next_product in range(indx + 1, N):  # 아직 처리 안한 제품들
        min_cost_for_product = float('inf')

        for factory in range(N):  # 모든 공장 확인
            if not visited[factory]:  # 아직 사용 안한 공장이라면
                # 이 제품을 이 공장에서 만드는 비용
                min_cost_for_product = min(min_cost_for_product, arr[next_product][factory])

        # 이 제품의 최소 생산 비용을 누적
        remaining_min += min_cost_for_product

    # 가지치기 조건: 현재 비용 + 남은 최소 비용 >= 이미 찾은 최솟값
    if cur_price + remaining_min >= min_price:
        return

    for factory in range(N):
        if visited[factory]:
            continue
        visited[factory] = True
        recur(indx+1, cur_price + arr[indx][factory])
        visited[factory] = False

T=int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [False]*N

    min_price = float('inf')

    recur(0,0)


    print(f'#{tc} {min_price}')