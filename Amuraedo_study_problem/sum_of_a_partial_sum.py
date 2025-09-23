"""
주어지는 수의 나열 즉 수열에서 주어진 S가 되는 경우 count를 세서
총 몇개인지 출력

"""


def finding(index, current_subset):
    global count, Num_list, N, S

    if index == N: #종료조건으로 index가 끝까지 탐색 완료되면 종료
        if len(current_subset) > 0 and sum(current_subset) == S: #빈경우 제외되도록 처리 + 합계에 해당하는 current_subset찾으면
            count += 1
        return
    # 포함시키지 않는 경우의 재귀
    finding(index + 1, current_subset)
    # 포함시키는 경우의 재귀
    current_subset.append(Num_list[index])
    finding(index + 1, current_subset)
    current_subset.pop()    #백트래킹


N,S = map(int,input().split())
Num_list = list(map(int,input().split()))
count = 0

finding(0,[])
print(count)

