##### N x N 배열에서 각 원소를 중심으로, 상하좌우 k칸의 합계 중 최대값 (k=2)
# 문제: "각 원소를 중심으로 상하좌우 k칸의 합계"
# → 중심값 + 상하좌우 k칸까지의 값들

# sum_result = arr[i][j]  # 중심값부터 시작
# 여기에 상하좌우 k칸을 더해감

max_v = 0   #상하좌우 중 가장 큰 값을 임의 설정
N = 4
K = 1
arr = [         # 배열도 정의 필요
    [1, 2, 3, 4],
    [5, 6, 7, 8], 
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

for i in range(N):
    for j in range(N):
        sum_result = arr[i][j]   
        for di, dj in [[-1,0],[1,0],[0,-1],[0,1]]: # di,di를 상하좌우 값 범위에서 반복 돌리기
            for c in range(1, K+1):
                ni, nj = i+di*c, i+dj*c
                if 0<=ni<N and 0<=nj<N:
                    sum_result += arr[ni][nj]
        if max_v < sum_result:
            max_v = sum_result

print(max_v)      


"""
예시 (k=2일 때):
    X
    X  
X X 중심 X X  # 중심 + 좌2칸 + 우2칸 + 상2칸 + 하2칸
    X
    X
"""

