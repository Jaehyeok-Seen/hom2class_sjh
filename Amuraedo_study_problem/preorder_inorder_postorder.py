def preorder_traversal(node,path):
    if node is None:
        return

    path.append(node)
    preorder_traversal(tree[node]['left'],path)
    preorder_traversal(tree[node]['right'], path)



def inorder_traversal(node,path):
    if node is None:
        return

    inorder_traversal(tree[node]['left'], path)
    path.append(node)
    inorder_traversal(tree[node]['right'], path)


def postorder_traversal(node,path):
    if node is None:
        return

    postorder_traversal(tree[node]['left'], path)
    postorder_traversal(tree[node]['right'], path)
    path.append(node)


"""
이진트리를 입력받아 전위순회, 중위순회, 후위 순회한 결과를 출력하는 프로그램을 작성

"""

N = int(input()) #노드의 개수
#항상 노트 A
tree = {}
for _ in range(N):
    node, left, right = input().split()
    tree[node] = {
        'left' : left if left != '.' else None,
        'right' : right if right != '.' else None
    }
preorder = []
inorder = []
postorder = []

preorder_traversal('A',preorder)
inorder_traversal('A',inorder)
postorder_traversal('A',postorder)

print(''.join(preorder))
print(''.join(inorder))
print(''.join(postorder))
