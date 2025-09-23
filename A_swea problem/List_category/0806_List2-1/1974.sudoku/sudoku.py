import sys
sys.stdin = open('input (1).txt')

T = int(input())
for tc in range(1,T+1):


    sudoku = [list(map(int,input().split())) for _ in range(9)]
    #print(sudoku)
    result = 1
    # 행이 같을 때 열 순회시켜서 num_list안에서 1개씩만 썼는지 확인
    for i in range(9):
        num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in range(9):
            if sudoku[i][j] in num_list:
                num_list.remove(sudoku[i][j])
            else:
                result = 0
                break

    # 열이 같을 때 행 순회시켜서 num_list안에서 1개씩만 썼는지 확인
    for j in range(9):
        num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(9):
            if sudoku[i][j] in num_list:
                num_list.remove(sudoku[i][j])
            else:
                result = 0
                break

    #delta 이용해서 3x3배열 확인하는거까지 해야 완료
    for center_i in range(0,9,3): # 시작 인덱스를 기준으로 델타 이용할거라 3x3이니 범위는 (0,9,3)
        for center_j in range(0,9,3):
            num_list = [1,2,3,4,5,6,7,8,9]

            for di in range(3): # 3x3배열 범위 이렇게
                for dj in range(3):
                    i = center_i + di
                    j = center_j + dj
                    if sudoku[i][j] in num_list:
                        num_list.remove(sudoku[i][j])
                    else:
                        result = 0
                        break

    print(f'#{tc} {result}')