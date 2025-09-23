class CQueue:
    def __init__(self, size = 10):
        self.front = 0
        self.rear = 0
        self.container = [0] * size
        self.size = size

    def is_full(self):
        #rear+1을 나머지연산한 값이 프론트라 같다면 풀이다
        return (self.rear+1) % self.size == self.front

    def is_empty(self):
        return self.rear == self.front

    def enQ(self, value):
        if self.is_full():
            raise TypeError('Queue is Full!')

        else:
            self.rear = (self.rear + 1) % self.size
            self.container[self.rear] = value

    def deQ(self):
        if self.is_empty():
            raise TypeError('Queue is Empty!')
        else:
            self.front = (self.front + 1) % self.size
            return self.container[self.front]

import sys
sys.stdin = open('input.txt')

T =10
for tc in range(1, T+1):
    _ = int(input())
    q = CQueue(9)  # front가 빈 칸이어야 함. 8개의 숫자 + 빈 칸
    # 숫자를 큐에 넣어 준다.
    for value in map(int, input().split()):
        # print(value)
        q.enQ(value)

    is_finish = False   #모든 연산이 종료되었는지 확인하는 변수

    while not is_finish:
        # deQ 하고 1~5까지 빼면서
        # 해당 값이 0 이상이면 enQ
        # 해당 값이 0 이하면 값을 0으로 하고 enQ 종료
        for i in range(1, 6):
            temp = q.deQ()
            temp -= i
            if temp > 0:
                q.enQ(temp)
            else:
                q.enQ(0)
                is_finish = True
                break
        pass

    print(f'#{tc}', end=' ')
    for _ in range(8):
        print(q.deQ(), end = ' ')
    print()