class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self,item):
        node = Node(item)

        if self.rear is None:
            self.front = node
            self.rear = node


        else:
            self.rear.next = node
            self.rear = node

        self.size += 1

    def dequeue(self):
        if self.front is None:
            raise IndexError('빈 큐에서 꺼낼 수 없음')

        temp = self.front

        self.front = self.front.next

        #꺼내고 나서 또 빌수도 있을 경우를 대비
        if self.front is None:
            self.rear = None

        self.size -= 1
        return temp.data
    # temp자체로는 노드이기 때문에 위로 따라가면서 temp는  self.front가 되고 self.front =node니까
    # node에서 데이터를 꺼내려면 self.front.data가 되어야한다.