"""
            W
        F        R
    O     T  , A     E
S
"""

# 위 트리를 in_order 형식으로 순회해 각 노드를 읽으면 특정 단어를 알 수 있다.
# 트리는 완전 이진 트리 형식으로 주어지며, 노드당 하나의 문자만 저장 가능

#정점 정보는 해당 정점의 문자, 해당 정점의 왼쪽 자식, 오른쪽 자식의 정점 번호 순서로 주어진다.
# 루트 정점의 번호는 항상 1이다.
#8
# 1 W 2 3
# 2 F 4 5
# 3 R 6 7
# 4 O 8
# 5 T
# 6 A
# 7 E
# 8 S
#1번 케이스의 예시를 보면 처음의 숫자, 처음 정점의 문자, 자식 정점의 숫자 2개


class Node:
    def __init__(self,data,str_data,left=None,right=None):
        self.data = data
        self.str_data = str_data
        self.left = left
        self.right = right

def inorder(node):
    if node:
        inorder(node.left)
        print(node.str_data, end ='')
        inorder(node.right)



import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1,T+1):
    V = int(input())
    information = [input().split() for _ in range(V)]
#[['1', 'N', '2', '3'], ['2', 'O', '4', '5'], ['3', 'T', '6', '7'], ['4', 'H', '8', '9'], ['5', 'T', '10', '11'], ['6', '_', '12', '13'], ['7', 'T', '14', '15'], ['8', 'E', '16', '17'], ['9', 'O', '18', '19'], ['10', 'Y', '20', '21'], ['11', 'A', '22', '23'], ['12', 'N', '24', '25'], ['13', 'N', '26', '27'], ['14', 'T', '28', '29'], ['15', 'E'], ['16', 'T'], ['17', 'C'], ['18', 'N'], ['19', 'L'], ['20', 'G'], ['21', '_'], ['22', 'R'], ['23', 'I'], ['24', 'I'], ['25', 'G'], ['26', 'I'], ['27', 'S'], ['28', 'I'], ['29', 'U']]

    nodes = {}
    #위 정보에서 각 정점별로 노드를 만들고 나서 관계설정까지 for문을 2번 돌려야함
    #1번째 for문 각 정점의 숫자 별로 노드 만들기
    for info in information:

        node_n = int(info[0])  # 첫번재는 노드의 숫자
        node_s = info[1]  # 두번째는 노드의 문자
        nodes[node_n] = Node(node_n, node_s)  # 클래스로 정의된 노드 불러와서 저장


    #2번째 for문 자녀 노드가 존재 할 경우 관계 설정
    for info in information: # 문제에서 주어지는 한케이스에서 반복되는 정보들 속에서 한개씩 정리
        node_n = int(info[0]) # 첫번재는 노드의 숫자

        if len(info) == 3:
            nodes[node_n].left = nodes[int(info[2])]  #nodes딕셔너리에 node_n키에 해당하는 left값이다.
        elif len(info) == 4:
            nodes[node_n].left = nodes[int(info[2])]    #left추가
            nodes[node_n].right = nodes[int(info[3])]   #right추가

    print(f'#{tc}', end=' ')
    inorder(nodes[1])
    print()


