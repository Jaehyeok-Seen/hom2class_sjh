import sys
sys.stdin = open('input (1).txt')

def DFS(list, cnt):
    global max_value
    if cnt <= 0:
        max_value = max(max_value, int(''.join(list)))
        return

    state = (''.join(list),cnt)

    if state in visited:
        return
    visited.add(state)

    n = len(list)

    for i in range(n):
        for j in range(i+1,n):
            if list[i] == list[j]:
                continue
            list[i],list[j] = list[j],list[i]
            DFS(list,cnt-1)
            list[i],list[j] = list[j],list[i]

T=int(input())
for tc in range(1,T+1):
    price, limit_cnt = input().split()
    num_list = list(price)
    limit_cnt = int(limit_cnt)

    max_value = 0
    visited = set()
    DFS(num_list,limit_cnt)
    print(f'#{tc} {max_value}')