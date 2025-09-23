"""
선형 큐
front : 가장 최근에 삭제된 원소의 인덱스입니다.
rear : 마지막으로 저장된 원소의 인덱스입니다.

상태표현
- 초기 상태 : front = rear = - 1
- 공백 상태 : front = rear
- 포화 상태 : rear == n-1 (n : 배열의크기, n-1 : 배열의 마지막 인덱스)

"""
class LinearQueue:
    def __init__(self,size):
        self.size = size
        self.q = [0] * size  # 고정 크기 배열
        self.front = -1
        self.rear = -1

    def is_full(self):
        return self.rear == self-1

    def is_empty(self):
        return self.front == self.rear

    def enqueue(self,item):
        if self.is_full():
            print("Queue_Full")
            return
        else:
            self.rear += 1
            self.q[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("Queue_Empty")
            return None
        else:
            self.front += 1
            return self.q[self.front]

    def peek(self):
        if self.is_empty():
            print("Queue_Empty")
        else:
            print("Queue:", self.q[self.front + 1:sefl.rear + 1])

    def qpeek(): #가장 앞에 있는 원소를 삭제 없이 반환하는 연산
        print(f"Peeking at : {front.item}") #로그 추가 가능능
        reurn front.item


#선형 큐의 구현
#create_queue()
q = [0] * n
front = -1
rear = -1

def enqueue(item) :
    global rear
    if q
        print("Queue_Full")
    else:
        rear += 1
        q[rear]
