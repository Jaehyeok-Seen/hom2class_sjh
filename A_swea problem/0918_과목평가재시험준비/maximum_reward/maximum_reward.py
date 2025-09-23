import sys
sys.stdin = open('input (1).txt')

"""
정해진 횟수만큼 change했을 때 최대 상금 금액
"""
def DFS(num_list, cnt):
    global max_value
    if cnt <= 0 :
        int_num_list = int(''.join(num_list))
        max_value = max(max_value,int_num_list)
        return

    state = (''.join(num_list),cnt)
    if state in visited:
        return
    visited.add(state)

    n = len(num_list)
    for i in range(n):
        for j in range(i+1,n):
            # 앞에서부터 비교해서 자리 바꾸기
            if num_list[i] == num_list[j]:
                continue

            num_list[i],num_list[j] = num_list[j],num_list[i]
            DFS(num_list, cnt-1)
            num_list[i],num_list[j] = num_list[j],num_list[i]



T=int(input())
for tc in range(1,T+1):
    price, limit_cnt = input().split()
    num_list = list(price)
    limit_cnt = int(limit_cnt)

    max_value = 0
    visited = set()
    DFS(num_list, limit_cnt)

    print(f'#{tc} {max_value}')
