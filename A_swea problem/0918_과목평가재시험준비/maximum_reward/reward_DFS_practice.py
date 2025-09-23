import sys
sys.stdin = open('input (1).txt')


def DFS(price_list, limit_cnt):
    global max_price
    if limit_cnt == 0:
        final_price = int("".join(price_list))
        max_price = max(max_price, final_price )
        return


    state = (''.join(price_list),limit_cnt)
    if state in visited:
        return
    visited.add(state)

    for i in range(len(price_list)):
        for j in range(i+1,len(price_list)):
            if price_list[i] == price_list[j]:
                continue
            price_list[i],price_list[j] =price_list[j],price_list[i]
            DFS(price_list,limit_cnt-1)
            price_list[i], price_list[j] = price_list[j], price_list[i]

    return

T= int(input())
for tc in range(1,T+1):
    information = list(map(int,input().split()))
    price_list = list(str(information[0]))
    limit = information[1]

    max_price = 0
    visited = set()
    DFS(price_list,limit)
    print(f'#{tc} {max_price}')