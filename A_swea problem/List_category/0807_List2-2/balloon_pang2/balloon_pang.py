# import sys
# sys.stdin = open('input1.txt')
# # 한개의 풍선을 선택해 터뜨렸을 때 날릴 수 있는 꽃가루 수 중 최댓값을 출력
# T = int(input())
# for tc in range(1,T+1):
#     N, M = tuple(map(int,input().split()))
#     # N x M행렬
#     num_list = [list(map(int,input().split())) for _ in range(N)]
#     maximum_sum = 0
#     for i in range(N):
#         for j in range(M):
#             center = num_list[i][j]
#             sum = 0
#             for di, dj in [[-1,0],[1,0],[0,-1],[0,1]]:
#                 ni, nj =  i+di, j+dj
#                 if  0<= ni < N and 0<= nj < M:
#                         sum += num_list[ni][nj]
#             result = center + sum
#             if maximum_sum < result :
#                 maximum_sum = result

#     print(f'#{tc} {maximum_sum}')


# ##실수 리스트
# """
# 1. 행렬 값 구할 때
# num_list[i,j]라는 실수함 num_list[i][j]
# 2. maximum_sum의 위치 자꾸 헷갈려한다.
# 3. 예외 범위 설정시 0부터 N,M미만으로 안하고 N이하 M이하로만함 
# 4. 결과값 출력 indentation계속 헷갈려함

# """


def selection_sort(arr,N):
    for i in range(N-1):
        min_idx = i
        for j in range(i+1,N):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i],arr[min_idx] = arr[min_idx],arr[i]
    return arr




# import sys
# sys.stdin = open('input1.txt')

T= int(input())
for tc in range(1,T+1):
    N = int(input())
    num_list = list(map(int,input().split()))
    sort_num_list = selection_sort(num_list, N)
    result = []
    count = 0
    while count <10 and len(sort_num_list) > 0 : # while문이 총 10번 돌아가도록 바꿔야함!
        count += 1
        result.append(sort_num_list[-1])
        sort_num_list.pop(-1)
        if count < 10 and len(sort_num_list) > 0:
            count += 1
            result.append(sort_num_list[0])
            sort_num_list.pop(0)
        else:
            break
    print(f'#{tc} {" ".join(map(str,result[:11]))}')
        
        

