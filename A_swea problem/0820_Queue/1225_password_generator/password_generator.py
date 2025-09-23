class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return f'{self.data}'
        """
        object at 0x000002A5B74..이렇게 나오는건 따로 정의해주지 않아서
        python이 정해둔 기본값으로 출력이 되는거다
        그렇다면 __str__ 을 호출해서 재정의해주면 변경이 가능하다는 뜻 
        f-string으로 나오게끔 정의하면 숫자로 출력되게 된다.
        """

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self,item):
        self.size += 1
        node = Node(item)

        if self.rear is None:
            self.front = node
            self.rear = node

        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.front is None:
            raise IndexError('queue is Empty')

        self.size -= 1

        temp = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None
        return temp.data

    def size(self):
        return self.size



"""
8개의 숫자를 입력받는다

첫번째 수를 1 감소한 뒤, 맨 뒤로 보낸다
그 다음 첫번째 수는 2 감소한 뒤 맨 뒤로,
그 다음 첫번째 수는 3 감소하고 맨뒤로,
그 다음 첫번째 수는 4 감소하고 맨뒤로,
그 다음 첫번째 수는 5 감소하고 맨뒤로,
이와 같은 작업을 한 싸이클이라 한다.(5까지 감소하면 한싸이클)

종료 시점 : 숫자가 감소할 때 0보다 작아지는 경우 0으로 유지되면서 종료
출력 값 : 이 때 8자리의 숫자 값이 암호
"""

import sys
sys.stdin = open('input.txt')

T = 10
for i in range(1, T+1):
    q = Queue()
    result = [0]*8
    tc = int(input())
    arr = list(map(int,input().split()))
    for indx in range(8):
        q.enqueue(arr[indx])    # 8자리의 숫자를 enqueue 잘 시킨 상태
        # print(q)
        #일단 1씩 감소시켜서 다시 enqueue하기

    finished = False #=>flag변수라고 한다 특정상황이 오면 스탑거는 방법

    while finished is False:

        for minus in range(1,6): # 한싸이클 내에서 -1,-2,-3,-4,-5를 구현하기 위해
            re = q.dequeue() - minus
            #re가 결과고 0보다 작으면 - 넣고


            if re <= 0:

                q.enqueue(0)
                finished = True
                break

            else:
                q.enqueue(re)

    for k in range(8):
        result[k] = q.dequeue()

    print(f'#{i}', *result)


    #완성되면 숫자를 변경해서 한 싸이클 구현
    #한싸이클을 무한 반복 돌리고 종료 시점 : 숫자가 감소할 때 0보다 작아지는 경우 0으로 유지되면서 종료

    #큐에 인풋받은 8자리 숫자를 차례대로 넣는다
    #dequeue할 때 -1
    # inque



