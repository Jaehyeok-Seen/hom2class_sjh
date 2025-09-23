import sys
sys.stdin = open('5209_input.txt')


def calculate(row,current_cost):
    global price, min_price
    remaining_min = sum(min_cost_per_row[row:])
    if current_cost + remaining_min >= min_price:
        return
    #=================================가지치기 완료
    if row == N:
        min_price = min(min_price,current_cost)
        return

    for col in range(N):
        if used[col]:
            continue

        used[col] = True
        calculate(row+1,current_cost + price[row][col])
        used[col] = False



T=int(input())
for tc in range(1,T+1):
    N = int(input())
    price = [list(map(int,input().split())) for _ in range(N)]
    min_price = float('inf')
    used = [False] * N
    min_cost_per_row = [min(row) for row in price]

    calculate(0,0)
    print(f'#{tc} {min_price}')