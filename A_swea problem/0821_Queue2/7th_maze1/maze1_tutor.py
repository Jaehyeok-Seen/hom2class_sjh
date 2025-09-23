import sys
sys.stdin = open('input.txt')

class cQueue:
    def __init__(self,size = 16):
        self.front = 0
        self.rear = 0
        self.container = [0] * size
        self.size = size   #len으로 할 수도 있지만 불필요한 연산 줄이기 위해

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def is_empty(self):
        return self.rear == self.front

    def enqueue(self, value):
        if self.is_full():
            raise ValueError('Queue is Full')
        else:
            self.rear = (self.rear + 1) % self.size
            self.container[self.rear] = value

    def dequeue(self):
        if self.is_empty():
            raise ValueError('Queue is empty!')
        else:
            self.front = (self.front + 1) % self.size
            return self.container[self.front]



T = 10
for tc in range(1,T+1):
    N = 16 #미로의 크기
    _ = input()
    maze = [(input()) for _ in range(N)]

    # 왔던 길을 표시하기 위한 리스트 ( 미로의 크기와 동일하게 초기화 )
    visited = [[False] * N for _ in range(N)]
    q = cQueue(N*N)    # 미로의 크기만큼 넉넉하게 queue 준비

    # result 변수를 미리 초기화( 경로를 찾지 못했을 때를 대비 )
    result = 0

    # 시작 위치를 찾기! 문자 '2'가 시작 위치
    for r in range(N):
        for c in range(N):
            if maze[r][c] == '2':
                # r, c가 시작 지점, Q에 넣고 미로 시작
                q.enqueue((r,c))
                break
    # BFS를 통해 모든 길을 탐색하고 도착지에 도착하면 즉시 종료
    # 큐가 비어있지 않다면!
    while not q.is_empty():
    # 큐에 있는 값을 dequeue
        row, col = q.dequeue()
    # 해당 값이 한 번도 방문하지 않았다면
        if not visited[row][col]:
    #   방문처리(도착지점인지 확인)
            visited[row][col] = True
            if maze[row][col] == '3':
                result = 1
                break
    #   연결된 다른 곳이 있는지 확인 ( 상, 하, 좌, 우 )
            for dr, dc in [(-1,0), (1,0) , (0,-1), (0,1)]:
                nr = row + dr
                nc = col + dc
                if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != '1':
    #   만약에 한번도 방문하지 않은 곳이라면
                    if not visited[nr][nc]:
    #   해당 위치를 enqueue
                        q.enqueue((nr,nc))

    print(f'#{tc}',result)