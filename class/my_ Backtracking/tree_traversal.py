arr = [1,2,1,3,2,4,3,5,3,6,4,7,5,8.9,6,10,6]

# [참고]graph 처럼 저장하는 방식
nodes = [[] for _ in range(17)]

for i in range(0, len(arr),2):
    parent_node = arr[i]
    child_node = arr[i+1]
    nodes[parent_node].append(child_node)

    #자식이 없는 걸 표현하기 위해 None 을 삽입
for li in nodes:
    for _ in range(len(li),2):
        li.append(None)

def order(node):
    if node == None:
        return

    # nodes[node] : node에 연결된 번호들 (자식 번호들 )
    # nodes[node][0] : 첫 번째 자식 번호
    # nodes[node][1] : 두 번째 자식 번호
    print(node, end=' ') # 전위 순회
    order(nodes[node][0])
    order(nodes[node][1])

class TreeNode :
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self,child):
        if (not self.left):
            self.left = child
            return
        if (not self.right):
            self.right = child
            return

        return