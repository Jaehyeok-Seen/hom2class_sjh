#Node 클래스 - 줄 서는 한 사람
class Node:
    def __init__(self, data, next=None):
        self.data = data  # 이 사람의 정보
        self.next = next # 뒤에 서있는 사람을 가리킴

class Queue:
    def __init__(self):
        self.front = None   #줄 맨 앞사람
        self.rear = None    #줄 맨 뒷사람
        self.size = 0       #총 몇명인지

    def enqueue(self, item):
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
            raise IndexError('비어있는 큐입니다.')

        temp = self.front

        self.front = self.front.next

        if self.front is None:
            self.rear = None

        self.size -= 1
        return temp.data







