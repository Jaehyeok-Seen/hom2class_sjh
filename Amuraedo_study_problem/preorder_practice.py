def preorder(node,list):
    if node is None:
        return

    list.append(node)
    preorder(tree[node]['left'],list)
    preorder(tree[node]['right'],list)


def inorder(node,list):
    if node is None:
        return

    inorder(tree[node]['left'],list)
    list.append(node)
    inorder(tree[node]['right'],list)

def postorder(node, list):
    if node is None:
        return

    postorder(tree[node]['left'], list)
    postorder(tree[node]['right'], list)
    list.append(node)

N = int(input())
tree = {}
for _ in range(N):
    node, left, right = input().split()
    tree[node]={
        'left' : left if left != '.' else None,
        'right' : right if right != '.' else None,
    }



preorder_list=[]
inorder_list = []
postorder_list= []

preorder('A',preorder_list)
inorder('A',inorder_list)
postorder('A',postorder_list)

print(''.join(preorder_list))
print(''.join(inorder_list))
print(''.join(postorder_list))