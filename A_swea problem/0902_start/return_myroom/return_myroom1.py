import sys
sys.stdin = open('sample_input.txt')

"""
move에 대한 함수 정의하는 방식으로 풀예정
def move(list):
    리스트를 풀어서 인덱스 값들끼리
    범위 겹치지 않으면 기본 단위시간은 1
    겹치는 순간마다 count += 1
    시작점과 목표지점이 다 정해져있음
    moving_list = 
    

"""
def move(students):
    global N
    time = 1

    # [[10, 20], [30, 40], [50, 60], [70, 80]]
    start = [0 for _ in range(N+1)]
    goal = [0 for _ in range(N + 1)]

    for i in range(N):
        path = students[i]
        start[i] = path[0]
        goal[i] = path[1]

    for i in range(N):
        for j in range(i+1,N):
            if start[i] < start[j] < goal[i]:
                time += 1
            elif start[i] < goal[j] < goal[i]:
                time += 1
            elif start[i] == goal[j] and goal[i] == start[j]:
                pass
            elif start[i] < start[j] < goal[i] and start[i] < goal[j] < goal[i]:
                time -=1

    return time


T = int(input())

for tc in range(1,T+1):
    N = int(input())

    moving_student = [list(map(int,input().split())) for _ in range(N)]
    """
    [[10, 20], [30, 40], [50, 60], [70, 80]]
    [[1, 3], [2, 200]]
    [[10, 100], [20, 80], [30, 50]]
    """
    result = move(moving_student)
    print(result)

