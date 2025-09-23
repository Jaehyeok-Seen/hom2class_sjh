class CircularQueue:
    def __init__(self, k: int):
        self.n = k + 1  # Full/Empty 구분을 위해 +1 (여유공간 생성)
        self.data = [0] * self.n
        self.front = 0  # 데이터를 꺼낼 위치
        self.rear = 0  # 데이터를 넣을 위치

    def enqueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.data[self.rear] = value  # ✅ rear에 추가
        self.rear = (self.rear + 1) % self.n  # ✅ rear 이동
        return True

    # def dequeue(self) -> bool: # 성공/ 실패만 알려주는 방식
    #     if self.isEmpty():
    #         return False
    #
    #     # 실제로는 값을 반환해야 함
    #     value = self.data[self.front]
    #     self.front = (self.front + 1) % self.n
    #     return True  # 또는 value 반환

    def dequeque(self) -> int:  # 실제 값을 반환하는 방식이 일반적
        if self.isEmpty():
            return -1 # -1 또는 None, 예외 발생

        value = self.data[self.front]  # 값을 읽는 과정
        self.front = (self.front + 1) % self.n
        return value


    def isEmpty(self) -> bool:
        return self.front == self.rear

    def isFull(self) -> bool:
        return (self.rear + 1) % self.n == self.front

#구체적인 예시로 이해하기
queue = CircularQueue(4)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)

print("큐 상태:", queue.data)
print("front:", queue.front)
print("rear:", queue.rear)

first_item = queue.dequeque() #10
print(f"처리할 작업: {first_item}")
