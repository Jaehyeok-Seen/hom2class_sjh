#NxN행렬에서 단어의 길이k가 들어갈 자리를 출력
#흑은 0, 백 = 1로 이루어진 곳이 글자가 들어갈 수 있음
# 0의 개수와 k의 수가 같아야함
# 가로 세로 구분해서 찾으면 됨
def find_space(arr,N,K):
    total_count = 0
    #가로 경우
    for i in range(N):
        count = 0
        for j in range(N):
        
            if arr[i][j] == 1: #행중심으로 돌렸을 때 1발견하면 카운트 올리기
                count += 1
            else:              #1이아닌 0을 만날 경우=연속된 1이 끝날 경우
                if count ==K:
                    total_count +=1
                count = 0

        if count == K: #0을 만나지 않고 벽을 만나 반복이 종료된 경우에도 check
            total_count += 1
    
    #세로 경우
    for j in range(N):
        count = 0
        for i in range(N):
            if arr[i][j] == 1: #행중심으로 돌렸을 때 1발견하면 카운트 올리기
                count += 1
            else:              #1이아닌 0을 만날 경우=연속된 1이 끝날 경우
                if count ==K:
                    total_count +=1 # 연속된 1이 종료됐을 때 누적된 count가 조건을 달성한 경우
                count = 0 # 다시 초기화해야함

        if count == K: #0을 만나지 않고 벽을 만나 반복이 종료된 경우에도 check
            total_count += 1

    return total_count



import sys
sys.stdin  = open('input-2.txt')

T = int(input())

for tc in range(1,T+1):
    N,K = map(int, input().split()) # NxN행렬, K :글자의 길이수
    puzzle = [list(map(int,input().split())) for _ in range(N)] #퍼즐

    result = find_space(puzzle,N,K)
    print(f'#{tc} {result}') 
    