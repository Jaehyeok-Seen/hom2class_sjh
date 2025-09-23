import sys
sys.stdin = open('5099_input.txt')

class CircleQueue:
    def __init__(self, size):
        self.queue = [None]*size
        self.front = 0
        self.rear = 0
        self.size = size

    def enqueue(self,data):
        if self.is_full():
            return False

        self.rear = (self.rear +1 ) % self.size
        self.queue[self.rear] = data
        return True
    def dequeue(self):
        if self.is_empty():
            return False

        data = self.queue[self.front]
        self.front = (self.front + 1) % self.size
        return data
    def is_full(self):
        return 
    def is_empty(self):
        return front == end

"""
피자는 1번위치에서 넣거나 뺀다
M개의 피자에 처음 뿌려진 치즈의 양
화덕을 한바퀴 돌때 녹지않은 치즈의 양은 반으로 줄어든다.
이전 치즈의 양을 C라고 하면 다시 꺼냈을 때 C//2로 줄어든다.
치즈가 모두 녹아 0이되는 즉시 꺼내고 바로 그자리에 남은 피자를 순서대로 넣는다.
"""

T = int(input())
for tc in range(1, T+1):
    N,M = map(int,input().split())
    #N = 화덕의 크기, M = 피자의 개수
    cheeze = list(map(int,input().split()))

    원형 큐 만들기
    큐의 front = rear면 비어있는거