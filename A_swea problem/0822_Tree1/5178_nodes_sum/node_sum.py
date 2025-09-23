"""
완전 이진 트리의 리프 노드에 1000이하의 자연수 저장
리프 노드를 제외한 노드에는 자식 노드에 저장된 값의 합이 들어있다.
N개의 노드를 갖는 트리의 루트는 1번
같은 단계에서는 왼쪽에서 오른쪽으로 증가,
단계가 꽉 차면 다음단계의 왼쪽부터 시작
문제: 리프 노드 번호와 저장된 값이 주어지면 나머지 노드에 자식 노드 값의 합을 저장한다음,
지정한 노드 번호에 저장된 값을 출력하는 프로그램을 작성
"""
class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
    def __str__(self):
        return f'Node(data = {self.data})'

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)

        if node.left and node.right :
            node.data = node.left.data + node.right.data
        elif node.left:
            node.data = node.left.data
import sys
sys.stdin = open('5178_input.txt')


T = int(input())


for tc in range(1,T+1):
    N, M, L = map(int,input().split())

    # N:노드의 개수
    # M: 리프 노드의 개수
    # L: 값을 출력할 노드 번호
    # 5 3 2
    # 4 1
    # 5 2
    # 3 3
    nodes = {}
    for i in range(1,1+N):
        nodes[i] = Node(0)
        #딕셔너리에 담아둘 node들 번호별로 만들어두고

    # i , nodes[i] = map(int,input().split())  #내가 실수한 부분, 동시에 다 받으려함 node는 객체인데..
    for _ in range(M):
        node_num, value = map(int,input().split())
        nodes[node_num].data = value


    #디버깅용
    # for i in range(1,N+1):
    #     print(f"{i}번 노드의 data = {nodes[i].data}")




    for i in range(1, N+1):
        left_child = 2 * i
        right_child = 2 * i + 1

        if left_child <= N:
            nodes[i].left = nodes[left_child]

        if right_child <= N:
            nodes[i].right = nodes[right_child]


    postorder(nodes[1])
    print(f'#{tc} {nodes[L].data}')



