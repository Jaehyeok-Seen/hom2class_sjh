#종료 조건 :  N개의 행을 모두 고려하면 종료
#가지의 수 :  N개의 열

def recur(row):
    if row == N:
        return

    for col in range(N):
        #col을 선택했다.
        path.append(col)
        reucur( row + 1 )
        path.pop()

N = 4
answer = 0
path = []

# ================================================================
#중복을 제거하는 순열과 동일
def recur(row):
    if row == N:
        return

    for col in range(N):
        if visited[col]:
            continue
        # col을 선택했다.
        visited[col] = 1
        path.append(col)
        recur(row + 1)
        path.pop()
        visited[col]= 0


N = 4
answer = 0
path = []
visited = []
# ======================================================================
#중복을 제거하는 순열과 동일
def recur(row):
    if row == N:
        return

    for col in range(N):
        # 가지치기 : 같은 열을 못 고르도록 했다면
        # => 유망하지 않은 케이스를 모두 삭제 ( 세로, 대각선 )
        if  check[row, col] is False:
            continue
        # col을 선택했다.
        visited[col] = 1
        path.append(col)
        recur(row + 1)
        path.pop()
        visited[col]= 0


N = 4
answer = 0
path = []
visited = []
# =========================================================================체크 구현
def check(row, col):
    # 1. 같은 열에 놓은 적이 있는가?
    for i in range(row):
        if visited[i][col]:
            return False  # 빠진 return False 추가

    # 2. 좌 상단 대각선에 놓은 적이 있는가?(\)
    i, j = row - 1, col - 1  # 좌표설정 먼저 해두고
    while i >= 0 and j >= 0:  # -1씩 하는과정을 while문으로
        if visited[i][j]:
            return False
        i -= 1
        j -= 1

    # [참고] for문으로 하고싶다!
    # for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
    #     if visited[i][j]:
    #         return False

    # 3. 우상단 대각선에 놓은 적이 있는가?(/)
    i, j = row - 1, col + 1
    while i >= 0 and j < N:
        if visited[i][j]:
            return False
        i -= 1
        j += 1

    # 위 3가지 조건을 다 통과한다면
    return True


# 중복을 제거하는 순열과 동일
def recur(row):
    global answer
    if row == N:
        answer += 1  # 해답 개수 증가
        return

    for col in range(N):
        # 가지치기 : 같은 열을 못 고르도록 했다면
        # => 유망하지 않은 케이스를 모두 삭제 (세로, 대각선)
        if check(row, col) is False:  # check 함수 호출 수정
            continue

        # col을 선택했다.
        visited[row][col] = 1
        path.append(col)
        recur(row + 1)
        path.pop()
        visited[row][col] = 0


N = 4
answer = 0
path = []
visited = [[0] * N for _ in range(N)]  # 2차원 리스트 초기화 추가

# 실행
recur(0)
print(f"N={N}일 때 가능한 경우의 수: {answer}")


# 실제로 해답을 보고 싶다면 아래 함수 사용
def print_solutions():
    global answer, solutions
    answer = 0
    solutions = []

    def recur_with_print(row):
        global answer
        if row == N:
            answer += 1
            solutions.append([row[:] for row in visited])  # 현재 상태 저장
            return

        for col in range(N):
            if check(row, col) is False:
                continue

            visited[row][col] = 1
            path.append(col)
            recur_with_print(row + 1)
            path.pop()
            visited[row][col] = 0

    recur_with_print(0)

    # 해답 출력
    for i, solution in enumerate(solutions):
        print(f"\n해답 {i + 1}:")
        for row in solution:
            print(' '.join('Q' if cell else '.' for cell in row))

# 해답 출력 (선택적)
# print_solutions()