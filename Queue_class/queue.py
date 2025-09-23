class Node:
    def __init__(self,data, next=None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

#큐의 맨 뒤에 요소를 추가하는 enqueque 메서드를 정의
    def enqueue(self, item):   # 큐에 저장할 데이터를 매개변수로 받는다.
        self.size += 1         # 큐에 새로운 요소를 추가하는 메서드이므로 enqueue에서는 사이즈 올린다.
        node = Node(item)      # 큐 내부의 링크드 리스트에 새 노드를 만들어 요소를 저장한다.
        if self.rear is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node


    def dequeue(self):
        if self.front is None:
            raise IndexError('pop from empty queue') # 비어있는데 요소를 꺼내려고 할경우 에러메시지
        self._size -= 1
        temp = self.front  #큐의 맨 앞에 있는 노드인 self.front를 임시 변수 temp에 저장해서
        # 나중에 내부의 링크드 리스트에서 노드를 제거한 뒤에도 참조 가능
        self.front = self.front.next
        # 그 다음에는 self.front.next에 self.front를 할당해서 큐 내부의 링크드 리스트에서 큐의
        # 맨앞에 있는 요소를 꺼낸다.
        if self.front is None:
            self.rear = None
        # 큐 맨 앞의 요소를 제거한 후 큐에 남아있는 요소가 없다면 self.rear에 None을 할당한다.
        return temp.data

    def size(self):
        return self.size